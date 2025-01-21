**Prompt used for AI**

"I'm interested in the Companies House API for all the endpoints. List all the endpoints."

**Here are the main endpoint categories and their specific endpoints:**

**Company Information**


*   GET /company/{company_number}                    # Basic company information
*   GET /company/{company_number}/officers           # Company officers
*   GET /company/{company_number}/filing-history     # Filing history
*   GET /company/{company_number}/insolvency        # Insolvency information
*   GET /company/{company_number}/charges           # Charges (mortgages)
*   GET /company/{company_number}/registers         # Register information
*   GET /company/{company_number}/uk-establishments # UK establishment details

**Officer Information**

*   GET /officers/{officer_id}                      # Individual officer details
*   GET /officers/{officer_id}/appointments         # Officer's appointments

**Search Endpoints**

*   GET /search/companies                           # Search companies
*   GET /search/officers                            # Search officers
*   GET /search/disqualified-officers               # Search disqualified officers
*   GET /advanced-search/companies                  # Advanced company search

**Filing History**

*   GET /company/{company_number}/filing-history/{transaction_id}  # Specific filing
*   GET /company/{company_number}/filing-history/categories        # Availabl categories

**Persons with Significant Control (PSC)**

*   GET /company/{company_number}/persons-with-significant-control # List PSCs
*   GET /company/{company_number}/persons-with-significant-control/individual/{psc_id}
*   GET /company/{company_number}/persons-with-significant-control/corporate-entity/{psc_id}
*   GET /company/{company_number}/persons-with-significant-control/legal-person/{psc_id}
*   GET /company/{company_number}/persons-with-significant-control/super-secure/{psc_id}
*   GET /company/{company_number}/persons-with-significant-control/statements

**Document/Image Retrieval**

*   GET /document/{document_id}                     # Get document metadata
*   GET /document/{document_id}/content            # Get document content

**Registered Office Address**

*   GET /company/{company_number}/registered-office-address  # Get registered office

**Company Profile**

*   GET /company/{company_number}/registers         # Company registers
*   GET /company/{company_number}/exemptions        # Company exemptions

**To use these endpoints, you need to:**

1. Register for an API key at the Companies House Developer Hub
2. Use Basic Authentication with your API key
3. Include appropriate headers:
*   Authorization: Basic <your-base64-encoded-api-key>
*   Accept: application/json

**Example Python code to make a request:**

```
import requests
import base64

def get_companies_house_data(endpoint, api_key):
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

# Example usage:
# api_key = "your_api_key_here"
# company_number = "12345678"
# data = get_companies_house_data(f"/company/{company_number}", api_key)
```

**Rate Limiting**

*   Standard rate limit: 600 requests per 5 minutes
*   Streaming rate limit: 600 requests per 5 minutes per IP address

Important Notes **bold text**:

*   All date-time fields are returned in ISO 8601 format
*   Company numbers should be padded with zeros to 8 characters
*   Some endpoints may require additional parameters
*   Responses are paginated where appropriate
*   Error responses follow standard HTTP status codes