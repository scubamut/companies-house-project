"""Top-level package for companies-house-project."""

__author__ = """daveg"""
__email__ = 'scubamut@gmail.com'
__version__ = '0.1.0'

from chtools.ch_basics import APIResponse, Config, CompanyData, RegisteredOffice
from chtools.ch_basics import get_endpoint_data, CompaniesHouseAPI, RateLimiter
from chtools.ch_utils import get_api_key, setup_logging
from chtools.ch_utils import explore_nested_json, robust_nested_json_to_multi_df, play_sound_until_input

from . import cli

# Add other names you want to expose
__all__ = [
    'get_api_key',
    'setup_logging',
    'get_endpoint_data',
    'APIResponse',
    'CompanyData',
    'CompaniesHouseAPI',
    'RateLimiter',
    'Config',
    'RegisteredOffice',
    'cli',
    'explore_nested_json',
    'robust_nested_json_to_multi_df',
    'play_sound_until_input'
    # Add other names you want to expose
]
