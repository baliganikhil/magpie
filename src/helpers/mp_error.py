import logging
import sys

def show_error(msg):
    print('')
    logging.critical("[Magpie Error]: %s" % (msg) )
    sys.exit()