import logging
from hilda_garde.settings import TOKEN, SETTINGS_MODULE, __version__
from core.commands import client


logging.basicConfig(level='INFO')
log = logging.getLogger()

if __name__ == '__main__':
    log.info(
        '''
        Init banner
        '''
    )
    log.info('Running Hilda Garde version: %s\n', __version__)

    client.run(TOKEN)
