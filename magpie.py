#!/usr/local/bin/python3

import logging
import sys
sys.path.insert(0, 'src/helpers')
sys.path.insert(0, 'src/server')
sys.path.insert(0, 'src/storage')
sys.path.insert(0, 'src/project')
sys.path.insert(0, 'src/utils')

print('')
print('Starting Magpie')
print('')

from mp_config import MagpieConfigHandler
from mp_files import MapgieFileHandler
from server_handler import MagpieServerHandler
from storage_handler import MagpieStorageHandler
from project_handler import MagpieProjectHandler

logging.basicConfig(level=logging.INFO)

config_path = 'config.json'
package_config_path = 'src/config/package_config.json'
magpie_config_handler = MagpieConfigHandler(config_path)
magpie_package_config_handler = MagpieConfigHandler(package_config_path)

magpie_config = magpie_config_handler.get_config()
magpie_package_config = magpie_package_config_handler.get_config()

MapgieFileHandler(magpie_config)
MagpieServerHandler(magpie_config)
MagpieStorageHandler(magpie_config, magpie_package_config)
MagpieProjectHandler(magpie_config)