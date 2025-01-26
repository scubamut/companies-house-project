from chtools.ch_utils import setup_logging, get_api_key
from chtools.ch_basics import Config, RateLimiter
from chtools.ch_basics.APIResponse import APIResponse
import logging
import base64
import requests
from typing import Optional, Dict, List, Any
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# logger = setup_logging()
# api_key = get_api_key()

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