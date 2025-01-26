def get_company_details(api_key, company_number):
    """
    Fetch company details from the UK Companies House API.

    Parameters:
    api_key (str): Your API key for the Companies House API.
    company_number (str): The company number to search for.

    Returns:
    dict: A dictionary containing the company details.
    """
    endpoint = f"/company/{company_number}"
    return get_companies_house_data(endpoint, api_key)