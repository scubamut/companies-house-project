

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