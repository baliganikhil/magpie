import logging
from express_handler import ExpressHandler

class MagpieNodeHandler:
    FRAMEWORK_SERVERLESS = 'express-serverless'

    def __init__(self, magpie_config, framework):
        logging.info('Handling nodejs with framework %s' % framework)

        if framework == self.FRAMEWORK_SERVERLESS:
            ExpressHandler()
