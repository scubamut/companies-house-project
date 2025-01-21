# CH_FUNCTIONS

CH_FUNCTIONS is a Python package to interact with the UK Companies House API.

## Installation

```bash
pip install CH_FUNCTIONS
```

## Usage

```bash
from CH_FUNCTIONS import get_company_details

api_key = 'your_api_key'
company_number = '12345678'

details = get_company_details(api_key, company_number)
print(details)
```

#### Building and Installing the Package Locally

Navigate to the root directory of your package and run the following commands to build and install your package locally:

```bash
python setup.py sdist bdist_wheel
pip install .
```

#### Using the Package in Jupyter Notebooks

```
Once the package is installed, you can import and use it in your Jupyter notebooks:

Python
from CH_FUNCTIONS import get_company_details

api_key = 'your_api_key'
company_number = '12345678'

details = get_company_details(api_key, company_number)
print(details)
```