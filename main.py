import logging
from hilda_garde.settings import TOKEN, __version__
from core.commands import client
from core.keep_alive import keep_alive


logging.basicConfig(level='INFO')
log = logging.getLogger()

if __name__ == '__main__':
    log.info(
        '''
        Init banner
        '''
    )
    log.info('Running Hilda Garde version: %s\n', __version__)
    keep_alive()
    client.run(TOKEN)
