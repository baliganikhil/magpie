import logging
from express_handler import ExpressHandler

class MagpieNodeHandler:
    magpie_config = {}

    FRAMEWORK_SERVERLESS = 'aws-serverless-express'

    def __init__(self, magpie_config, framework):
        logging.info('Handling nodejs with framework %s' % framework)

        self.magpie_config = magpie_config;

        if framework == self.FRAMEWORK_SERVERLESS:
            ExpressHandler(self.magpie_config)
