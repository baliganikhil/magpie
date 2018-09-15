import logging
from subprocess import call
from mp_config import MagpieConfigHandler

class ExpressHandler:
    magpie_config = {}

    def __init__(self, magpie_config):
        logging.info('Handling Express')
        self.magpie_config = magpie_config

        self.installExpressServerless()

    def installExpressServerless(self):
        target_folder = self.magpie_config[MagpieConfigHandler.KEY_TARGET_FOLDER]
        aws_serverless_package_name = self.magpie_config[MagpieConfigHandler.KEY_SERVER][MagpieConfigHandler.KEY_FRAMEWORK]

        call(["sh", "src/server/sh/serverless_install.sh", target_folder, aws_serverless_package_name])
