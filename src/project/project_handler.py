import logging
import os

from mp_config import MagpieConfigHandler
from config_utils import MagpieConfigUtils

class MagpieProjectHandler:
    magpie_config = {}

    def __init__(self, magpie_config):
        logging.info("Handling Project")
        self.magpie_config = magpie_config
        self.magpie_config_utils = MagpieConfigUtils(self.magpie_config)

        self.addStorageConnection()

    def createFolderStructure(self):
        pass

    def addStorageConnection(self):
        logging.info("Adding Storage Connection")
        server_lang = self.magpie_config_utils.getServerLanguage()
        storage = self.magpie_config_utils.getStorage()

        if server_lang == MagpieConfigHandler.LANG_NODEJS and storage == MagpieConfigHandler.DB_MONGODB:
            self.addStorageConnNodejsMongodb()

    def addStorageConnNodejsMongodb(self):
        logging.info("Adding MongoDB connection info for NodeJS app")
        filename = os.path.join(self.magpie_config_utils.getTargetFolder(), 'app.js')

        mongoose_import_line = "var mongoose = require('mongoose');"
        mongoose_conn_line = '''
            var mongo_connection_url = "mongodb://localhost:27017";
            mongoose.connect(process.env.MONGO_URL || mongo_connection_url);
        '''

        import_line_no = 2
        conn_line_no = 3

        f = open(filename, 'r')
        contents = f.readlines()
        f.close()

        contents.insert(import_line_no, mongoose_import_line)
        contents.insert(conn_line_no, mongoose_conn_line)
        contents = ''.join(contents)

        f = open(filename, 'w')
        f.write(contents)
        f.close()