# WORKS OK!!

import chtools
print('I imported companies_house!')
import chtools.ch_basics
print ('I imported ch_basics')
import chtools.ch_utils
print ('I imported ch_utils')
from chtools.ch_basics import Config, CompanyData, RegisteredOffice
from chtools.ch_basics import get_endpoint_data, APIResponse, CompaniesHouseAPI, RateLimiter
from chtools.ch_utils import get_api_key, setup_logging, explore_nested_json
from chtools.ch_utils import explore_nested_json, robust_nested_json_to_multi_df, play_sound_until_input

from chtools import get_api_key, setup_logging
from chtools import get_endpoint_data, APIResponse, CompanyData, CompaniesHouseAPI, RateLimiter
from chtools import Config, RegisteredOffice
from chtools import explore_nested_json, robust_nested_json_to_multi_df, play_sound_until_input

print(chtools.__all__)