class CompanyData(BaseModel):
    company_number: str
    company_name: str
    company_status: str
    date_of_creation: str
    registered_office_address: str
    sic_codes: str