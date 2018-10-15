import copy

from .utils.constantsdefine import *

class TrieToken:

    def __init__(self):

        self.root = TrieNodeToken(0)

    def insertTrieNode(self, nameCode, obj):
        dummpy = self.root
        for i in range(len(nameCode)*2):
            val = 0
            if i % 2 == 0:
                val = (nameCode[i//2]) & 0x0F
            else:
                val = ((nameCode[i//2]) >> 4) & 0x0F
            if not dummpy.childrenArray[val] is None:
                dummpy = dummpy.childrenArray[val]
            else:
                nextnode = TrieNodeToken(val)
                dummpy.childrenArray[val] = nextnode
                dummpy = nextnode
        dummpy.addObject(obj)
        return True

    def searchTrieNode(self, nameCode):
        dummpy = self.root

        i = 0

        while i < len(nameCode)*2:
            val = 0
            if i % 2 == 0:
                val = nameCode[i // 2] & 0x0F
            else:
                val = (nameCode[i // 2] >> 4) & 0x0F

            if dummpy.childrenArray[val] is None:
                break

            dummpy = dummpy.childrenArray[val]
            i += 1

        if i == len(nameCode)*2:
            return dummpy
        else:
            return None






class TrieNodeToken:


    def __init__(self, value=0):
        self.object = None
        self.value = value
        self.isLeaf = False
        self.childrenArray = [None for i in range(16)]


    def setLeaf(self, isLeaf):
        self.isLeaf = isLeaf

    def setObject(self, object):
        self.setLeaf(True)
        self.object = object

    def addObject(self, object):
        if self.object is None:
            self.object = []
            self.setLeaf(True)
        self.object.append(object)

    def removeValue(self):
        self.setLeaf(False)
        self.object = None

    def getObject(self):
        return self.object

class TrieApplication:

    @staticmethod
    def MatchTrieTokenWithOverlap(trieToken, str):
        matchList = []
        if str == "":
            return matchList
        begin = 0
        end = 1
        nodeMax = None
        strMatchMax = ""
        str = str + " "
        wordModelList = []
        while begin < len(str):
            if end > len(str):
                matchList.append(wordModelList)
                wordModelList = []
                begin += 1
                end = begin + 1
                continue
            strMatch = str[begin:end]
            node = trieToken.searchTrieNode(bytes(strMatch, encoding='utf-8'))
            if node is None:
                if not nodeMax is None:

                    matchList.append(wordModelList)
                    wordModelList = []
                    begin += 1
                    end = begin + 1
                    nodeMax = None
                else:
                    matchList.append(wordModelList)
                    wordModelList = []
                    begin += 1
                    end = begin + 1
            elif node.getObject() is None:
                end += 1
            else:
                tokenModelList = node.getObject()
                if len(tokenModelList) > 0:
                    end += 1
                    nodeMax = node
                    strMatchMax = strMatch
                    for aToken in tokenModelList:
                        aTokenCopy = copy.deepcopy(aToken)
                        aTokenCopy.wordStr = strMatch
                        wordModelList.append(aTokenCopy)

        matchList.pop(len(matchList) - 1)
        return matchList


    @staticmethod
    def MatchTriePatternWithOverlap(triePattern, segmentList):
        result = []

        for startIndex in range(len(segmentList)):
            aResult = []
            TrieApplication.DFSForMatchTriePatternWithOverlap(triePattern, segmentList, startIndex, startIndex, [], aResult)
            result.append(aResult)

        return result


    @staticmethod
    def DFSForMatchTriePatternWithOverlap(triePattern, segmentList, startIndex, currentIndex, wordModelList, result):
        if currentIndex >= len(segmentList):
            return
        for wordModel in segmentList[currentIndex]:
            wordModelList.append(wordModel)
            nodeList = triePattern.searchTrieNode(list(map(lambda x:x.entityType, wordModelList)))
            isMatch = False
            for node in nodeList:
                if not node is None:
                    isMatch = True
                    if node.isLeaf:
                        entityWord = ""
                        for aWord in wordModelList:
                            entityWord += aWord.wordStr

                        dic = node.getObject()
                        for akey in dic:
                            aPattern = dic[akey]
                            aPatternCopy = copy.deepcopy(aPattern)
                            aPatternCopy.initializeExtract()
                            aPatternCopy.wordStr = entityWord
                            for i in range(len(wordModelList)):
                                aWord = copy.deepcopy(wordModelList[i])
                                aWord.entityType = node.namePath[i]
                                aPatternCopy.addSubWordModel(aWord)

                            result.append(aPatternCopy)

            if isMatch:
                TrieApplication.DFSForMatchTriePatternWithOverlap(triePattern, segmentList, startIndex, wordModel.endPos, wordModelList, result)

            wordModelList.pop(len(wordModelList) -1)








class TrieNodePattern:

    def __init__(self, value):
        self.setValue(value)
        self.childrenArray = []
        self.forbidArray = set()
        self.isLeaf = False
        self.object = None
        self.namePath = []

    def setValue(self, value):
        self.value = value
        self.valueWithoutNum = value.split(SYMBOL_ENTITYTYPE_NUMBER_BREAK)[0]

    def setLeaf(self, isLeaf):
        self.isLeaf = isLeaf

    def getValue(self):
        return self.value

    def getObject(self):
        return self.object

    def addObject(self, object):
        if self.object is None:
            self.object = {}
            self.setLeaf(True)
        self.object[object.entityType] = object

    def addChildWithoutCheck(self, node):
        self.childrenArray.append(node)

    def getChildByExact(self, name):
        for node in self.childrenArray:
            if node.value == name:
                return node

        return None

    def getChildByFuzzy(self, name):
        nodeList = []
        for node in self.childrenArray:
            if node.valueWithoutNum == name:
                nodeList.append(node)

        return nodeList



class TriePattern:

    def __init__(self):
        self.root = TrieNodePattern("")

    def insertTrieNode(self, namePath, obj):
        dummpy = self.root
        for name in namePath:
            if name.endswith("!"):
                nameNude = name.split("!")[0]
                dummpy.forbidArray.add(nameNude)
                continue

            node = dummpy.getChildByExact(name)
            if not node is None:
                dummpy = node
            else:
                nextnode = TrieNodePattern(name)
                dummpy.addChildWithoutCheck(nextnode)
                dummpy = nextnode

        dummpy.namePath = copy.deepcopy(namePath)
        dummpy.addObject(obj)

        return True

    def searchTrieNode(self, nameList):
        results = []
        self.DFSForSearchTrieNode(nameList, 0, self.root, results)
        return results


    def DFSForSearchTrieNode(self, nameList, namePos, dummpy, results):
        if namePos >= len(nameList):
            results.append(dummpy)
            return

        if nameList[namePos] in dummpy.forbidArray:
            return

        for dummpyNext in dummpy.getChildByFuzzy(nameList[namePos]):
            self.DFSForSearchTrieNode(nameList, namePos+1, dummpyNext, results)

        for dummpyNext in dummpy.getChildByFuzzy("?"):
            self.DFSForSearchTrieNode(nameList, namePos+1, dummpyNext, results)

        for dummpyNext in dummpy.getChildByFuzzy("*"):
            i = 1
            while namePos + i <= len(nameList):
                self.DFSForSearchTrieNode(nameList, namePos + i, dummpyNext, results)
                i += 1









