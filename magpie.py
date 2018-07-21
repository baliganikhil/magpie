import logging
import sys
sys.path.insert(0, 'src/helpers')

print('')
print('Starting Magpie')
print('')

from mp_config import MagpieConfigHandler

logging.basicConfig(level=logging.INFO)

config_path = 'config.jsn'
MagpieConfigHandler(config_path)