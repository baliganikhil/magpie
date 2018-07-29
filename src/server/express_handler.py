import logging
from subprocess import call

class ExpressHandler:
    def __init__(self):
        logging.info('Handling Express')
        self.installExpressServerless()

    def installExpressServerless(self):
        # call(["sh", "sh/serverless_install.sh"])
        call(["echo", "sh/serverless_install.sh"])
