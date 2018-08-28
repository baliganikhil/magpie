import json
import logging
from mp_error import show_error

class MagpieConfigHandler:
    config_path = ''
    magpie_config = {}

    KEY_TARGET_FOLDER = 'target_folder'
    KEY_SERVER = 'server'
    KEY_LANGUAGE = 'language'
    KEY_FRAMEWORK = 'framework'

    LANG_NODEJS = 'nodejs'

    def __init__(self, config_path):
        logging.info('Starting Magpie Config Handler')
        self.load_config(config_path)
        self.config_path = config_path

    def load_config(self, config_path):
        logging.info('Loading config from config path')
        try:
            config_file = open(config_path, 'r')
            self.magpie_config = json.load(config_file)
        except:
            show_error('Could not load the config file: %s' % (config_path) )

    def get_config(self):
        logging.info('Getting config')
        return self.magpie_config