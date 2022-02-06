"""
Main global settings and configs.
"""
from decouple import config

__version__ = '0.0.2'

TOKEN = config('TOKEN', '')
SETTINGS_MODULE = config('SETTINGS_MODULE', 'common')
DB_HOST = config('REPLIT_DB_URL')
DB_KEY = config('DB_KEY')

ENDPOINTS = {
    'campaigns': 'https://search.battlefy.com/homepage/campaigns/active?gameSlug=&&',
    'tournaments': 'https://dtmwra1jsgyb0.cloudfront.net/tournaments/'
}
