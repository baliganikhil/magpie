#!/usr/local/bin/python3

import logging
import sys
sys.path.insert(0, 'src/helpers')
sys.path.insert(0, 'src/server')

print('')
print('Starting Magpie')
print('')

from mp_config import MagpieConfigHandler
from mp_files import MapgieFileHandler
from server_handler import MagpieServerHandler

logging.basicConfig(level=logging.INFO)

config_path = 'config.json'
magpie_config_handler = MagpieConfigHandler(config_path)

magpie_config = magpie_config_handler.get_config()

MapgieFileHandler(magpie_config)
MagpieServerHandler(magpie_config)