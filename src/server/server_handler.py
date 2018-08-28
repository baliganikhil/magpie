import logging
import sys
from node_handler import MagpieNodeHandler
from mp_config import MagpieConfigHandler

class MagpieServerHandler:
    magpie_config = {}

    def __init__(self, magpie_config):
        logging.info('Handling server')
        self.magpie_config = magpie_config
        self.installServer()

    def installServer(self):
        if MagpieConfigHandler.KEY_SERVER not in self.magpie_config:
            logging.info('No server configuration found. Skipping...')
            print('No server configuration found. Skipping...')
            return

        server_config = self.magpie_config[MagpieConfigHandler.KEY_SERVER]
        if MagpieConfigHandler.KEY_LANGUAGE not in server_config:
            logging.critical('Key: %s is not present in the %s config' % (MagpieConfigHandler.KEY_LANGUAGE, MagpieConfigHandler.KEY_SERVER))
            sys.exit()
            return

        if MagpieConfigHandler.KEY_FRAMEWORK not in server_config:
            logging.critical('Key: %s is not present in the %s config' % (MagpieConfigHandler.KEY_FRAMEWORK, MagpieConfigHandler.KEY_SERVER))
            sys.exit()
            return

        if server_config[MagpieConfigHandler.KEY_LANGUAGE]:
            MagpieNodeHandler(self.magpie_config, server_config[MagpieConfigHandler.KEY_FRAMEWORK])
