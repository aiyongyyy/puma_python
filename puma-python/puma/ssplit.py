from .utils.fileutils import *
from .utils.constantsdefine import *
from .config import puma_config
from .model import *

import copy
import os

class QuerySsplit:

    def __init__(self):

        self.splitBlackList = {}
        for line in loadListFile(os.path.dirname(os.path.abspath(__file__)) + "/" + puma_config.BLACKLIST_FILE):
            if not line or line.startswith(SYMBOL_COMMENT_PERFIX):
                continue
            words = line.split("\t")
            if words[0] in self.splitBlackList:
                self.splitBlackList[words[0]].add(words[1])
            else:
                aSet = set()
                aSet.add(words[1])
                self.splitBlackList[words[0]] = aSet


    def SsplitQueryBySymbol(self, queryModel, stopList):
        stopIndexList = []
        stopIndexList.append(0)
        stopIndexList.append(len(queryModel.querySentence))
        for stop in stopList:
            index = 0
            while index > -1:
                index = queryModel.querySentence.find(stop, index + 1)
                if index > -1:
                    stopIndexList.append(index)

        # stopIndexList.sort()

        for i in range(len(stopIndexList) - 1):
            aQuery = self.getSubSegmentList(queryModel, stopIndexList[i], stopIndexList[i+1])
            if aQuery:
                queryModel.ssplitQueryModel.append(aQuery)

        return True


    def getSubSegmentList(self, queryModel, startPos, endPos):
        subSegmentList = []
        for i in range(startPos, endPos):
            aSegment = []
            for j in range(len(queryModel.wordModelList[i])):
                aWord = queryModel.wordModelList[i][j]
                if aWord.endPos <= endPos:
                    aWordCopy = copy.deepcopy(aWord)
                    aWordCopy.startPos = aWordCopy.startPos - startPos
                    aWordCopy.endPos = aWordCopy.endPos - startPos
                    aSegment.append(aWordCopy)

            subSegmentList.append(aSegment)

        if len(subSegmentList) > 0:
            aQuery = QueryModel()
            aQuery.querySentence = queryModel.querySentence[startPos:endPos]
            aQuery.wordModelList = subSegmentList
            return aQuery

        return None






puma_querySsplit = QuerySsplit()


