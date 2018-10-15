from .trie import *
from .config import puma_config
from .utils import fileutils
from .utils import constantsdefine
from .scene import puma_scenePool
from .data import puma_dataDictionary
from .model import TokenModel
from .scene import *

import logging
import json
import os

class Tokenize:

    def __init__(self):
        self.trieToken = TrieToken()
        self.initializeToken()

    def setTrieToken(self, trieToken):
        self.trieToken = trieToken

    def initializeToken(self):
        trieToken = TrieToken()
        InitializeTokenizeFile.InitializeTokenizeDict(trieToken)
        # if puma_config.DICT_NER_OPEN == 1:                                    not need now
        #     InitializeTokenizeSQL.InitializeTokenizeSQLTickerAB(trieToken);
        self.setTrieToken(trieToken)
        return True

    def TokenizeQuery(self, queryModel):

        results = TrieApplication.MatchTrieTokenWithOverlap(self.trieToken, queryModel.querySentence)

        for i in range(len(queryModel.wordModelList)):
            for wordModel in results[i]:
                queryModel.addWordModel(wordModel, i)

        return True






class InitializeTokenizeFile:

    def __init__(self):
        pass

    @staticmethod
    def InitializeTokenizeDict(trieToken):
        for file in puma_config.TOKENIZE_FILES.split(","):
            lines = fileutils.loadListFile(os.path.dirname(os.path.abspath(__file__)) + "/" + puma_config.TOKENIZE_PREFIX + file + puma_config.TOKENIZE_SUFFIX, "utf-8")
            TAG = None
            SCENE = None

            for line_num in range(len(lines)):
                line = lines[line_num].strip()

                if not line or line.startswith(constantsdefine.SYMBOL_COMMENT_PERFIX):
                    continue
                elif line.find("SCE:") == 0:
                    SCENE = puma_scenePool.getSceneByName(line[4:])
                elif SCENE is None:
                    logging.error("[ERROR] InitializeTokenizeFile error for no scene, define scene first! in file:{}:{}".format(file, line_num))
                    raise Exception
                elif line.startswith("TAG:"):
                    TAG = line[4:]
                    continue
                elif TAG is None or not TAG:
                    logging.error("[ERROR] InitializeTokenizeFile error for no TAG. in file:%s:%d".format(file, line_num));
                    raise Exception

                input = line.split("\t")
                word = input[0].lower()

                jsonObject = None
                if len(input) == 2:
                    jsonObject = json.loads(input[1])

                    if "value" in jsonObject:
                        jsonObject["sceneName"] = SCENE
                        jsonObject["entityType"] = TAG

                wordSynonymSet = set()
                if word in puma_dataDictionary.synonyMap:
                    wordSynonymSet = puma_dataDictionary.synonyMap[word]
                else:
                    wordSynonymSet.add(word)

                for wordSynonym in wordSynonymSet:
                    aToken = TokenModel()
                    aToken.entityType = TAG
                    aToken.scene = SCENE
                    aToken.wordStr = wordSynonym
                    aToken.json = jsonObject
                    if not trieToken.insertTrieNode(bytes(aToken.wordStr, encoding='utf-8'), aToken):
                        logging.error("[ERROR] InitializeTokenizeFile error for rule conflict. in file:{}:{}".format(file, line_num))
                        raise Exception

            if len(lines) > 0:
                logging.info("add token {} successfully".format(file))
            else:
                logging.error("add token {} error for find no file".format(file))

        return True


puma_tokenize = Tokenize()





