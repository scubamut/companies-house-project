class InsuranceCompanyFinder:
    """Main class for finding and processing insurance companies."""
    
    def __init__(self, api: CompaniesHouseAPI, logger: logging.Logger):
        self.api = api
        self.logger = logger
        self.company_names: List[str] = []  # Only store company names
    
    def is_insurance_company(self, sic_codes: List[str]) -> bool:
        """Check if company is an insurance company based on SIC codes."""
        return any(code.startswith(prefix) for prefix in Config.INSURANCE_SIC_CODES 
                  for code in sic_codes if code)
    
    def process_company(self, company_number: str, company_name: str) -> None:
        """Process a single company."""
        if company_name in self.company_names:  # Check for duplicate names
            return
            
        company_details = self.api.get_company_details(company_number)
        if not company_details:
            return
            
        sic_codes = company_details.get('sic_codes', [])
        if not self.is_insurance_company(sic_codes):
            return
            
        self.company_names.append(company_name)
        self.logger.info(f"Added company: {company_name}")
    
    def search_all_companies(self) -> List[str]:
        """Search and return all insurance company names."""
        for search_term in Config.SEARCH_TERMS:
            self.logger.info(f"\nSearching for: {search_term}")
            start_index = 0
            
            while start_index < Config.MAX_RESULTS:
                results = self.api.search_companies(search_term, start_index)
                if not results or not results.items:
                    break
                
                self.logger.info(f"Processing {len(results.items)} results starting at index {start_index}")
                
                for company in results.items:
                    company_number = company.get('company_number')
                    company_name = company.get('title')
                    if company_number and company_name:
                        self.process_company(company_number, company_name)
                
                if len(results.items) < Config.ITEMS_PER_PAGE:
                    break
                    
                start_index += Config.ITEMS_PER_PAGE
            
            self.logger.info(f"Completed search for term: {search_term}")
        
        return sorted(self.company_names)