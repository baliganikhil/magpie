import logging
import os

import mp_config
from mp_config import MagpieConfigHandler

from mp_error import show_error

class MapgieFileHandler:
    target_path = ''

    MagpieConfigHandler.KEY_TARGET_FOLDER = 'target_folder'

    def __init__(self, magpie_config):
        logging.info('Starting Magpie File Handler')
        self.create_project_folder_structure(magpie_config)
        pass

    def create_project_folder_structure(self, magpie_config):
        if MagpieConfigHandler.KEY_TARGET_FOLDER not in magpie_config:
            show_error('Config does not have target folder specified. Missing key: %s' % MagpieConfigHandler.KEY_TARGET_FOLDER)

        target_folder_path = magpie_config[MagpieConfigHandler.KEY_TARGET_FOLDER]

        # Check if target exists
        if os.path.exists(target_folder_path):
            logging.info('Target %s already exists' % target_folder_path)

            # Exists, but is not a directory
            if not os.path.isdir(target_folder_path):
                show_error('Target [%s] exists but is not a directory' % target_folder_path)

        else:
            # Target does not exist
            logging.info('Target %s does not exist. Creating...' % target_folder_path)
            os.makedirs(target_folder_path)
            pass
