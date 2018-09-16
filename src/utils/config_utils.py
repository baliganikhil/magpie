import logging
import sys
from mp_config import MagpieConfigHandler
from mp_error import show_error

class MagpieConfigUtils:
    magpie_config = {}

    def __init__(self, magpie_config):
        self.magpie_config = magpie_config

    def getServerLanguage(self):
        if MagpieConfigHandler.KEY_SERVER not in self.magpie_config:
            logging.info('No server configuration found. Skipping...')
            print('No server configuration found. Skipping...')
            return

        server_config = self.magpie_config[MagpieConfigHandler.KEY_SERVER]
        if MagpieConfigHandler.KEY_LANGUAGE not in server_config:
            logging.critical('Key: %s is not present in the %s config' % (MagpieConfigHandler.KEY_LANGUAGE, MagpieConfigHandler.KEY_SERVER))
            sys.exit()
            return

        return server_config[MagpieConfigHandler.KEY_LANGUAGE]

    def getStorage(self):
        if MagpieConfigHandler.KEY_STORAGE not in self.magpie_config:
            logging.info('No storage configuration found. Skipping...')
            print('No storage configuration found. Skipping...')
            return

        storage_config = self.magpie_config[MagpieConfigHandler.KEY_STORAGE]
        if MagpieConfigHandler.KEY_DB not in storage_config:
            logging.critical('Key: %s is not present in the %s config' % (MagpieConfigHandler.KEY_DB, MagpieConfigHandler.KEY_STORAGE))
            sys.exit()
            return

        return storage_config[MagpieConfigHandler.KEY_DB]

    def getTargetFolder(self):
        if MagpieConfigHandler.KEY_TARGET_FOLDER not in self.magpie_config:
            show_error('Config does not have target folder specified. Missing key: %s' % MagpieConfigHandler.KEY_TARGET_FOLDER)

        target_folder_path = self.magpie_config[MagpieConfigHandler.KEY_TARGET_FOLDER]
        return target_folder_path
