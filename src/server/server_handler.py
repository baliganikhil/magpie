import logging
import sys
from node_handler import MagpieNodeHandler

class MagpieServerHandler:
    magpie_config = {}
    KEY_SERVER = 'server'
    KEY_LANGUAGE = 'language'
    KEY_FRAMEWORK = 'framework'

    LANG_NODEJS = 'nodejs'

    def __init__(self, magpie_config):
        logging.info('Handling server')
        self.magpie_config = magpie_config
        self.installServer()

    def installServer(self):
        if self.KEY_SERVER not in self.magpie_config:
            logging.info('No server configuration found. Skipping...')
            print('No server configuration found. Skipping...')
            return

        server_config = self.magpie_config[self.KEY_SERVER]
        if self.KEY_LANGUAGE not in server_config:
            logging.critical('Key: %s is not present in the %s config' % (self.KEY_LANGUAGE, self.KEY_SERVER))
            sys.exit()
            return

        if self.KEY_FRAMEWORK not in server_config:
            logging.critical('Key: %s is not present in the %s config' % (self.KEY_FRAMEWORK, self.KEY_SERVER))
            sys.exit()
            return

        if server_config[self.KEY_LANGUAGE]:
            MagpieNodeHandler(self.magpie_config, server_config[self.KEY_FRAMEWORK])
