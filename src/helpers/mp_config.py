import json
import logging
from mp_error import show_error

class MagpieConfigHandler:
    config_path = ''
    magpie_config = {}

    def __init__(self, config_path):
        logging.info("Starting Magpie Config Handler")
        self.load_config(config_path)
        self.config_path = config_path
        pass

    def load_config(self, config_path):
        try:
            config_file = open(config_path, 'r')
            self.magpie_config = json.load(config_file)
        except:
            show_error('Could not load the config file: %s' % (config_path) )