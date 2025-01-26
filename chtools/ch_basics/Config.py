from pathlib import Path

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
    OUTPUT_DIR = Path("insurance_companies_data")