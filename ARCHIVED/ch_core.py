"""Core functionality for Companies House API interactions."""
import requests
import pandas as pd
import time
import logging
from typing import Optional, List, Dict, Any
from pydantic import BaseModel

from companies_house.ch_utils.setup_logging import setup_logging

# Add other imports needed by this file

# Set up logging
logger = setup_logging()
# set level
logger.setLevel(logging.INFO)

# Configuration class
class Config:
    # API Settings
    BASE_URL = "https://api.companieshouse.gov.uk"
    MAX_RESULTS = 1000
    ITEMS_PER_PAGE = 100
    
    # Rate Limiting
    MAX_REQUESTS = 590
    TIME_WINDOW = 300  # seconds
    
    # SIC Codes for Insurance Companies
    INSURANCE_SIC_CODES = ['651', '652']
    
    # Search Terms
    SEARCH_TERMS = [
        "insurance company",
        "insurance limited",
        "insurance ltd",
        "insurance plc",
        "assurance company",
        "assurance limited",
        "assurance ltd",
        "assurance plc"
    ]
    
    # Output Directory
    # OUTPUT_DIR = Path("insurance_companies_data")

# Data Models
class RegisteredOffice(BaseModel):
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    locality: Optional[str] = None
    postal_code: Optional[str] = None

class APIResponse(BaseModel):
    items: List[Dict[str, Any]]
    total_results: Optional[int] = None
    page_number: Optional[int] = None
    kind: Optional[str] = None

class CompanyData(BaseModel):
    company_number: str
    company_name: str
    company_status: str
    date_of_creation: str
    registered_office_address: str
    sic_codes: str

class CompaniesHouseAPI:
    """Handler for Companies House API interactions."""
    
    def __init__(self, api_key: str, logger: logging.Logger):
        self.api_key = api_key
        self.logger = logger
        # Pass logger to RateLimiter
        self.rate_limiter = RateLimiter(Config.MAX_REQUESTS, Config.TIME_WINDOW, logger)
        self.session = self._create_session()
        
        # Create base64 encoded authentication
        auth = base64.b64encode(f"{api_key}:".encode('ascii')).decode('ascii')
        self.headers = {
            'Authorization': f'Basic {auth}',
            'Accept': 'application/json'
        }
    
    @staticmethod
    def _create_session() -> requests.Session:
        """Create a session with retry strategy."""
        session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)
        return session
    
    def search_companies(self, search_term: str, start_index: int = 0) -> Optional[APIResponse]:
        """Search for companies using the Companies House API."""
        params = {
            'q': search_term,
            'items_per_page': Config.ITEMS_PER_PAGE,
            'start_index': start_index,
            'company_status': 'active'
        }
        
        try:
            self.rate_limiter.wait_if_needed()
            
            if start_index >= Config.MAX_RESULTS:
                self.logger.info(f"Reached maximum results limit ({Config.MAX_RESULTS}) for search term: {search_term}")
                return APIResponse(items=[])
            
            response = self.session.get(
                f"{Config.BASE_URL}/search/companies",
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            return APIResponse(**response.json())
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error making request: {e}")
            return None
    
    def get_company_details(self, company_number: str) -> Optional[Dict[str, Any]]:
        """Get detailed information for a specific company."""
        try:
            self.rate_limiter.wait_if_needed()
            
            response = self.session.get(
                f"{Config.BASE_URL}/company/{company_number}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching details for company {company_number}: {e}")
            return None

class RateLimiter:

    """Implements rate limiting for API requests."""
    
    def __init__(self, max_requests: int, time_window: int, logger: logging.Logger):
        self.max_requests = max_requests
        self.time_window = time_window
        self.logger = logger  # Add logger as instance variable
        self.requests: deque = deque()
    
    def can_make_request(self) -> bool:
        now = datetime.utcnow()
        while self.requests and self.requests[0] < now - timedelta(seconds=self.time_window):
            self.requests.popleft()
        
        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False
    
    def wait_if_needed(self) -> int:
        current_requests = len(self.requests)
        if current_requests >= self.max_requests:
            self.logger.info(f"Rate limit reached. Current requests in window: {current_requests}")
        
        while not self.can_make_request():
            self.logger.debug(f"Waiting for rate limit. Current requests: {len(self.requests)}")
            time.sleep(1)
        
        current_requests = len(self.requests)
        self.logger.debug(f"Request allowed. Current requests in window: {current_requests}")
        return current_requests

# get_data_from_endpoint
def get_endpoint_data(endpoint, api_key):
    """
    Fetch data from the UK Companies House API.

    Parameters:
    endpoint (str): The endpoint of the API.
    api_key (str): Your API key for the Companies House API.

    Returns:
    dict: The JSON response from the API.
    """
    base_url = "https://api.company-information.service.gov.uk"
    auth = base64.b64encode(f"{api_key}:".encode('ascii')).decode('ascii')
    
    headers = {
        'Authorization': f'Basic {auth}',
        'Accept': 'application/json'
    }
    
    response = requests.get(
        f"{base_url}{endpoint}",
        headers=headers
    )
    
    return response.json()