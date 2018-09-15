import logging
import sys
from subprocess import call
from mp_config import MagpieConfigHandler

class MagpieMongoHandler:
    magpie_config = {}
    magpie_package_config = {}

    def __init__(self, magpie_config, magpie_package_config):
        logging.info("Handling mongodb")
        self.magpie_config = magpie_config
        self.magpie_package_config = magpie_package_config
        self.installHelpers()

    def installHelpers(self):
        server_language = self.magpie_config[MagpieConfigHandler.KEY_SERVER][MagpieConfigHandler.KEY_LANGUAGE]
        db = self.magpie_config[MagpieConfigHandler.KEY_STORAGE][MagpieConfigHandler.KEY_DB]

        if server_language not in self.magpie_package_config:
            logging.critical('Key: %s is not present in the package config' % server_language)
            sys.exit()
            return

        mongoose_packages = self.magpie_package_config[server_language][MagpieConfigHandler.KEY_STORAGE][db]

        # NodeJS
        if server_language == MagpieConfigHandler.LANG_NODEJS:
            mongoose_package_list = []
            for mongoose_package in mongoose_packages:
                mongoose_package_version = mongoose_packages[mongoose_package]
                mongoose_package_list.append(mongoose_package + "@" + mongoose_package_version)

            mongoose_package_list = ' '.join(mongoose_package_list)
            target_folder = self.magpie_config[MagpieConfigHandler.KEY_TARGET_FOLDER]
            call(["sh", "src/storage/sh/mongoose_install.sh", target_folder, mongoose_package_list])

