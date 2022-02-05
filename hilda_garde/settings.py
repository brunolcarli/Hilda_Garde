"""
Main global settings and configs.
"""
from decouple import config

__version__ = '0.0.1'

TOKEN = config('TOKEN', '')
SETTINGS_MODULE = config('SETTINGS_MODULE', 'common')

ENDPOINTS = {
    'campaigns': 'https://search.battlefy.com/homepage/campaigns/active?gameSlug=&&',
    'tournaments': 'https://dtmwra1jsgyb0.cloudfront.net/tournaments/'
}
