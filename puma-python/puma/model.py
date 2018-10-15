from .scene import *
from .utils.constantsdefine import *
from .state import *

import re
import datetime

class WordModel:

    def __init__(self, wordStr, startPos, endPos, entityType):
        self.wordStr = wordStr
        self.startPos = startPos
        self.endPos = endPos
        self.entityType = entityType
        self.scene = SceneBase_Segment

    def merge(self, wordModel):
        pass


class TokenModel(WordModel):

    def __init__(self):
        self.json = None
        self.actualValue = None
        self.entityTypeNum = ""



class QueryModel:

    def __init__(self, querySentence=""):
        self.IS_SEARCH = True
        self.querySentence = querySentence
        self.segWords = []
        self.wordModelList = []
        self.ssplitQueryModel = []
        self.wordModelMaximize = []


        if self.IS_SEARCH:
            self.querySentence = self.preProcess("^" + querySentence + "$")
            for i in range(len(self.querySentence)):
                self.wordModelList.append([])
            self.addWordModel(WordModel("^", 0, 1, "^"), 0)
            self.addWordModel(WordModel("$", len(self.querySentence) - 1, len(self.querySentence), "$"), len(self.querySentence) -1 )
        else:
            self.querySentence = self.preProcess(querySentence)
            for i in range(len(self.querySentence)):
                self.wordModelList.append([])


    def preProcess(self, content):
        if content:
            return content.strip()
        else:
            return ""

    def addWordModel(self, wordModel, index):
        wordModel.startPos = index
        wordModel.endPos = index + len(wordModel.wordStr)
        if not self.CheckAlphabetValid(wordModel) or not self.CheckArabicValid(wordModel):
            return False
        aSegment = self.wordModelList[index]
        isMerge = False
        for aWord in aSegment:
            if aWord.wordStr == wordModel.wordStr and aWord.entityType == wordModel.entityType:
                aWord.merge(wordModel)
                isMerge = True
                break

        if not isMerge:
            aSegment.append(wordModel)
        return True

    def getWordModelByEntityType(self, type, index):
        if index < 0 or index >= len(self.wordModelList):
            return None
        aWordList = self.wordModelList[index]
        longetIndex = -1
        for i in range(len(aWordList)):
            aWord = aWordList[i]
            if aWord.entityType == type:
                if longetIndex == -1 or len(aWordList[i].wordStr)>len(aWordList[longetIndex].wordStr):
                    longetIndex = i

        if longetIndex == -1:
            return None
        else:
            return aWordList[longetIndex]


    def CheckAlphabetValid(self, wordModel):
        if re.match(r"[a-zA-Z].*", wordModel.wordStr) and wordModel.startPos != 0 and re.match(r".{" + (wordModel.startPos - 1) + "}[a-zA-Z].*", self.querySentence):
            return False
        if re.match(r"[a-zA-Z].*", wordModel.wordStr) and wordModel.endPos != len(self.querySentence) - 1 and re.match(r".{" + (wordModel.startPos - 1) + "}[a-zA-Z].*", self.querySentence):
            return False
        return True

    def CheckArabicValid(self, wordModel):
        if re.match(r"\\d.*", wordModel.wordStr) and wordModel.startPos != 0 and re.match(r".{" + (wordModel.startPos - 1) + "}\\d.*", self.querySentence):
            return False
        if re.match(r".*\\d", wordModel.wordStr) and wordModel.endPos != len(self.querySentence) - 1 and re.match(r".{" + (wordModel.endPos) + "}\\d.*", self.querySentence):
            return False
        return True

    def mergeSsplitQueryModel(self):
        self.wordModelList = []
        for aQuery in self.ssplitQueryModel:
            self.wordModelList.extend(aQuery.wordModelList)
            self.wordModelMaximize.extend(aQuery.wordModelMaximize)

        return True

class ParseModel(WordModel):

    def __init__(self):
        self.parseMap = {}


class PatternModel(WordModel):

    def __init__(self):
        self.cons = []
        self.subWordModels = []
        self.stateMap = {}

    def addSubWordModel(self, wordModel):
        isMerge = False
        for subWordModel in self.subWordModels:
            if subWordModel.wordStr == wordModel.wordStr and subWordModel.entityType == wordModel.entityType:
                subWordModel.merge(wordModel)
                isMerge = True
                break
        if not isMerge:
            self.subWordModels.append(wordModel)
        return True

    def initializeExtract(self):
        self.subWordModels = []
        self.stateMap = {}
        return True



class EntityDateModel:


    def __init__(self, value=None):

        if value is None:
            self.year = 0
            self.month = 0
            self.day = 0
            self.updateDate()
        elif isinstance(value, datetime.datetime):
            self.dateTime = value
            self.year = value.year
            self.month = value.month
            self.day = value.day
            self.updateDate()
        elif isinstance(value, str):
            if value.find("年") >= 0:
                self.year = int(re.sub("年|\\d{0,2}月|\\d{0,2}日", "", value))
            else:
                self.year = datetime.datetime.now().year

            if value.find("月") >= 0:
                self.month = int(re.sub("\\d{0,4}年|月|\\d{0,2}日", "", value))
            else:
                self.month = datetime.datetime.now().month

            if value.find("日") >= 0:
                self.day = int(re.sub("\\d{0,4}年|\\d{0,2}月|日", "", value))
            else:
                self.day = datetime.datetime.now().day

            self.updateDate()


    def updateDate(self):
        if self.year == 0:
            self.year = 1
        if self.month == 0:
            self.month = 1
        if self.day == 0:
            self.day = 1

        dateStr = str(self.year) + "-" + str(self.month) + "-" + str(self.day)
        try:
            self.dateTime = datetime.datetime(self.year, self.month, self.day)
            return
        except Exception as e:
            self.day -= 1
            self.updateDate()



class ParseMapModel:

    def __init__(self):
        self.state_parsing_map = {}

    def setVariableValue(self, nameWithScene, value):

        stateModel = puma_stateCtrl.stateMap[nameWithScene]

        if not self.state_parsing_map:
            map = {}
            map[stateModel.name] = value
            self.state_parsing_map[stateModel.scene.getSceneName()] = map
        elif not stateModel.scene.getSceneName() in self.state_parsing_map:
            map = {}
            map[stateModel.name] = value
            self.state_parsing_map[stateModel.scene.getSceneName()] = map
        else:
            map = self.state_parsing_map[stateModel.scene.getSceneName()]
            map[stateModel.name] = value
            self.state_parsing_map[stateModel.scene.getSceneName()] = map





