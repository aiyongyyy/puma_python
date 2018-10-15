

from .config import puma_config
from .utils.fileutils import *
from .utils.constantsdefine import *

import os

import logging

class DataDictionary:

    def __init__(self):
        self.synonyMap = {}
        self.initializeSynonym()
        pass

    def initializeSynonym(self):
        self.synonyMap = {}
        lines = loadListFile(os.path.dirname(os.path.abspath(__file__)) + "/" + puma_config.SYNONYM_FILE)
        for line_num in range(len(lines)):
            line = lines[line_num].strip()
            if not line or line.startswith(SYMBOL_COMMENT_PERFIX):
                continue

            wordSet = set(line.split("\t"))
            for word in wordSet:
                self.synonyMap[word] = wordSet

        logging.info("add Synonym {} successfully".format(len(self.synonyMap)))

        return True



puma_dataDictionary = DataDictionary()