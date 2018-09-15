import logging
import sys
from mp_config import MagpieConfigHandler
from mongo_handler import MagpieMongoHandler

class MagpieStorageHandler:
    magpie_config = {}
    magpie_package_config = {}

    def __init__(self, magpie_config, magpie_package_config):
        logging.info("Handling storage")
        self.magpie_config = magpie_config
        self.magpie_package_config = magpie_package_config
        self.handleStorage()

    def handleStorage(self):
        if MagpieConfigHandler.KEY_STORAGE not in self.magpie_config:
            logging.info('No storage configuration found. Skipping...')
            print('No storage configuration found. Skipping...')
            return

        storage_config = self.magpie_config[MagpieConfigHandler.KEY_STORAGE]
        if MagpieConfigHandler.KEY_DB not in storage_config:
            logging.critical('Key: %s is not present in the %s config' % (
            MagpieConfigHandler.KEY_DB, MagpieConfigHandler.KEY_STORAGE))
            sys.exit()
            return

        if storage_config[MagpieConfigHandler.KEY_DB] == MagpieConfigHandler.DB_MONGODB:
            MagpieMongoHandler(self.magpie_config, self.magpie_package_config)

