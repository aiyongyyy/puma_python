from .trie import *
from .config import puma_config
from .utils.fileutils import *
from .scene import puma_scenePool
from .model import *
from .utils import listutils
from .dynamic import *

import math
import logging
import copy

import os

class ExtractPattern:



    def __init__(self):

        self.extractRepeatTimes = 5


        triePattern = TriePattern()

        InitializeExtractionPattern.initializeExtractPatternFile(triePattern)

        self.setTriePattern(triePattern)

    def setTriePattern(self, triePattern):
        self.triePattern = triePattern

    def ExtractQuery(self, queryModel):
        repeat = self.extractRepeatTimes

        while repeat > 0:

            results = TrieApplication.MatchTriePatternWithOverlap(self.triePattern, queryModel.wordModelList)

            for i in range(len(queryModel.wordModelList)):
                for wordModel in results[i]:
                    queryModel.addWordModel(wordModel, i)

            repeat -= 1

        return True



class ExtractToMaxList:

    def __init__(self):
        pass

    def toMaxList(self, queryModel):

        scores = []

        results = []

        scores.append(0)
        results.append([])
        for i in range(1, len(queryModel.wordModelList) + 1):
            scoreMax = -1
            result = None
            for j in range(i):
                for wordModel in queryModel.wordModelList[j]:
                    if wordModel.startPos == j and wordModel.endPos == i:
                        if scores[j] < 0:
                            continue
                        score = scores[j] + int(math.pow(wordModel.endPos - wordModel.startPos, 2))
                        if score > scoreMax:
                            scoreMax = score
                            result = copy.deepcopy(results[j])
                            result.append([])
                            result[len(result) - 1].append(wordModel)
                        elif score == scoreMax:
                            wordModelPrev = result[len(result) - 1][0]
                            comp = comparatorEntityType.compare(wordModel, wordModelPrev)
                            if comp == 0:
                                result[len(result) - 1].append(wordModel)
                            elif comp > 0:
                                result = copy.deepcopy(results[j])
                                result.append([])
                                result[len(result) - 1].append(wordModel)
            scores.append(scoreMax)
            results.append(result)

        queryModel.wordModelMaximize = results[len(results) - 1]
        return True





class ExtractFilter:

    @staticmethod
    def selectExtractionParse(objects, predict):

        parseModelResultList = []

        for object in objects:
            if isinstance(object, ParseModel):
                if predict(object):
                    parseModelResultList.append(object)

        return parseModelResultList

    @staticmethod
    def selectExtractionPattern(objects, predict):
        patternModelResultList = []

        for object in objects:
            if isinstance(object, PatternModel):
                if predict(object):
                    patternModelResultList.append(object)

        return patternModelResultList

    @staticmethod
    def selectExtractionToken(objects, predict):
        tokenModelResultList = []

        for object in objects:
            if isinstance(object, TokenModel) and not isinstance(object, PatternModel):
                if predict(object):
                    tokenModelResultList.append(object)

        return tokenModelResultList



class comparatorEntityType:

    entityTypes = {}
    entityTypeExtraction = "extraction"

    entityTypes["single"] = 1
    entityTypes["segment"] = 2
    entityTypes["symbol"] = 3

    @staticmethod
    def compare(wordModel1, wordModel2):
        entityType1 = wordModel1.entityType
        entityType2 = wordModel2.entityType
        wordStr1 = wordModel1.wordStr
        wordStr2 = wordModel2.wordStr
        if len(wordStr1) < len(wordStr2):
            return 1
        elif len(wordStr1) > len(wordStr2):
            return -1
        else:
            int1 = comparatorEntityType.entityTypes[entityType1.split("_")[0]] if entityType1.split("_")[0] in comparatorEntityType.entityTypes else None
            int2 = comparatorEntityType.entityTypes[entityType2.split("_")[0]] if entityType2.split("_")[0] in comparatorEntityType.entityTypes else None

            if int1 is None and int2 is None:
                return 0
            elif int1 is None:
                return  1
            elif int2 is None:
                return -1
            else:
                if int1 == int2:
                    return 0
                elif int1 < int2:
                    return -1
                else:
                    return 1




class InitializeExtractionPattern:

    @staticmethod
    def initializeExtractPatternFile(triePattern):
        for file in puma_config.EXTRACT_FILES.split(","):
            if InitializeExtractionPattern.initializePatternRule(file, triePattern):
                logging.info("add extraction {} successfully".format(file))
            else:
                logging.error("add token {} error for find no file".format(file))


    @staticmethod
    def initializePatternRule(file, triePattern):
        GID = None
        SCENE = None
        load_state = STATE_LOAD_FILE.SLF_NORMAL
        lines = loadListFile(os.path.dirname(os.path.abspath(__file__)) + "/" + puma_config.EXTRACT_PREFIX + file + puma_config.EXTRACT_SUFFIX)
        patternModel = None
        con_act = None
        for line_num in range(len(lines)):
            line = lines[line_num].strip()
            if not line or line.startswith(SYMBOL_COMMENT_PERFIX):
                continue
            elif line.find("SCE:") == 0:
                SCENE = puma_scenePool.getSceneByName(line[4:])
            elif SCENE is None:
                logging.error("[ERROR] initializePattern error for no scene, define scene first! in file:{}:{}".format(file, line_num))
                raise Exception
            elif line.find("GID:") == 0:
                GID = line[4:]
                patternModel = PatternModel()
                patternModel.entityType = GID
                patternModel.scene = SCENE
                continue
            elif GID is None or not GID:
                logging.error("[ERROR] initializePattern error for no gid, must define gid! in file:{}:{}".format(file, line_num))
                raise Exception
            elif line.find("PAT:") == 0:
                if load_state != STATE_LOAD_FILE.SLF_NORMAL:
                    logging.error("[ERROR] initializePattern error for load state error, check condition PAT END! in file:{}:{}".format(file, line_num))
                    raise Exception
                sub = line[4:].split("\t")
                InitializeExtractionPattern.DFSforInitializeTriePattern(sub, 0, [], patternModel, triePattern)
            elif line.find("IF:") == 0:
                if load_state != STATE_LOAD_FILE.SLF_NORMAL or GID is None:
                    logging.error("[ERROR] initializePattern error for load state error, check condition IF END! in file:%s:%d", file, line_num)
                    raise Exception

                con_act = ConditionAction()
                patternModel.cons.append(con_act)
                load_state = STATE_LOAD_FILE.SLF_IF
            elif line.find("THEN:") == 0:
                if load_state != STATE_LOAD_FILE.SLF_IF_OK or GID is None or con_act is None or patternModel is None:
                    logging.error("[ERROR] initializePattern error for THEN state error, please check config !in file:{}:{}".format(file, line_num))
                    raise Exception
                load_state = STATE_LOAD_FILE.SLF_THEN
            elif line.find("ELSE:") == 0:
                if load_state != STATE_LOAD_FILE.SLF_THEN_OK or GID is None or con_act is None or patternModel is None:
                    logging.error("[ERROR] initializePattern error for ELSE state error, please check config !in file:{}:{}".format(file, line_num))
                    raise Exception
                load_state = STATE_LOAD_FILE.SLF_ELSE
            elif line.find("END") == 0:
                if (load_state != STATE_LOAD_FILE.SLF_THEN_OK and load_state != STATE_LOAD_FILE.SLF_ELSE_OK) or GID is None or con_act is None or patternModel is None:
                    logging.error("[ERROR] initializePattern error for END state error, please check config !in file:{}:{}".format(file, line_num))
                    raise Exception
                load_state = STATE_LOAD_FILE.SLF_NORMAL

            else:
                if load_state == STATE_LOAD_FILE.SLF_IF:
                    new_condition = Condition()

                    if not new_condition.initializeCondition(SCENE, line):
                        logging.error("[ERROR] initializePattern error for initialize IF expression, please check config !in file:{}:{}".format(file, line_num))
                        raise Exception


                    con_act.setCondition(new_condition)
                    load_state = STATE_LOAD_FILE.SLF_IF_OK
                    continue

                if load_state == STATE_LOAD_FILE.SLF_THEN:
                    load_state = STATE_LOAD_FILE.SLF_THEN_OK

                if load_state == STATE_LOAD_FILE.SLF_THEN_OK:

                    new_action_then = Action()
                    if not new_action_then.initializeAction(SCENE, line):
                        logging.error("[ERROR] initializePattern error for initialize THEN expression, please check config !in file:{}:{}".format(file, line_num))
                        raise Exception

                    con_act.addActionIf(new_action_then)
                    continue

                if load_state == STATE_LOAD_FILE.SLF_ELSE:
                    load_state = STATE_LOAD_FILE.SLF_ELSE_OK

                if load_state == STATE_LOAD_FILE.SLF_ELSE_OK:

                    new_action_else = Action()
                    if not new_action_else.initializeAction(SCENE, line):
                        logging.error("[ERROR] initializePattern error for initialize ELSE expression, please check config !in file:{}:{}".format(file, line_num))
                        raise Exception
                    con_act.addActionElse(new_action_else)
                    continue


                logging.error("[ERROR] initializePattern error for unknown line expression!in file:{}:{}".format(file, line_num))
                raise Exception

        if len(lines) > 0:
            return True
        else:
            return False






    @staticmethod
    def DFSforInitializeTriePattern(inputLineSegment, pos, namePath, patternModel, triePattern):
        if pos >= len(inputLineSegment):
            triePattern.insertTrieNode(namePath, patternModel)
            return
        name = inputLineSegment[pos].strip()
        if name == "[":
            endPos = listutils.getElementIndexFromIndex(inputLineSegment, lambda a : a == "]", pos)
            for i in range(pos + 1, endPos):
                InitializeExtractionPattern.DFSforInitializeTriePatternParseWildCard(inputLineSegment[i], inputLineSegment, endPos, namePath, patternModel, triePattern)
        elif name == "<":
            endPos =  listutils.getElementIndexFromIndex(inputLineSegment, lambda a : a == ">", pos)
            permutationList = listutils.getPermutation(inputLineSegment[pos + 1 : endPos])
            for permutation in permutationList:
                inputLineSegmentNew = []
                inputLineSegmentNew.extend(inputLineSegment[0:pos])
                inputLineSegmentNew.extend(permutation)
                inputLineSegmentNew.extend(inputLineSegment[endPos + 1 : len(inputLineSegment)])
                InitializeExtractionPattern.DFSforInitializeTriePattern(inputLineSegmentNew, pos, namePath, patternModel, triePattern)
        else:
            InitializeExtractionPattern.DFSforInitializeTriePatternParseWildCard(name, inputLineSegment, pos, namePath, patternModel, triePattern)



    @staticmethod
    def DFSforInitializeTriePatternParseWildCard(name, inputLineSegment, pos, namePath, patternModel, triePattern):
        if name == "":
            InitializeExtractionPattern.DFSforInitializeTriePattern(inputLineSegment, pos+1, namePath, patternModel, triePattern)
        elif name.endswith("?"):
            InitializeExtractionPattern.DFSforInitializeTriePattern(inputLineSegment, pos+1, namePath, patternModel, triePattern)

            nameNude = name.split("?")[0]
            if nameNude == ".":
                nameNude = "?"
            namePath.append(nameNude)
            InitializeExtractionPattern.DFSforInitializeTriePattern(inputLineSegment, pos+1, namePath, patternModel, triePattern)
            namePath.pop(len(namePath) - 1)
        elif name.endswith("+"):
            nameNude = name.split("+")[0]
            if nameNude == ".":
                nameNude = "*"
            namePath.append(nameNude)
            InitializeExtractionPattern.DFSforInitializeTriePattern(inputLineSegment, pos+1, namePath, patternModel, triePattern)
            namePath.pop(len(namePath) - 1)
        elif name.endswith("*"):
            InitializeExtractionPattern.DFSforInitializeTriePattern(inputLineSegment, pos+1, namePath, patternModel, triePattern)

            nameNude = name.split("\*")[0]
            if nameNude == ".":
                nameNude = "*"
            namePath.append(nameNude)

            InitializeExtractionPattern.DFSforInitializeTriePattern(inputLineSegment, pos+1, namePath, patternModel, triePattern)
            namePath.pop(len(namePath) - 1)
        elif re.match(".*\\{\\d\\}", name):

            nameNude = name.split("\\{|\\}")[0]
            if nameNude == ".":
                nameNude = "?"

            n = int(name.split("\\{|\\}")[1])

            for i in range(n):
                namePath.append(nameNude)

            InitializeExtractionPattern.DFSforInitializeTriePattern(inputLineSegment, pos + 1, namePath, patternModel, triePattern)
            for i in range(n):
                namePath.pop(len(namePath) - 1)
        elif re.match(".*\\{\\d,\\d\\}", name):
            nameNude = name.split("\\{|\\}|,")[0]

            if nameNude == ".":
                nameNude = "?"
            m = int(name.split("\\{|\\}|,")[1])
            n = int(name.split("\\{|\\}|,")[2])

            for i in range(m):
                namePath.append(nameNude)

            for i in range(n - m + 1):
                InitializeExtractionPattern.DFSforInitializeTriePattern(inputLineSegment, pos + 1, namePath, patternModel, triePattern)
                namePath.append(nameNude)

            for i in range(n+1):
                namePath.pop(len(namePath) - 1)

        else:
            namePath.append(name)
            InitializeExtractionPattern.DFSforInitializeTriePattern(inputLineSegment, pos + 1, namePath, patternModel, triePattern)
            namePath.pop(len(namePath) - 1)



class ParsePattern:

    def __init__(self):
        pass

    def ParseQueryByPattern(self, patternModel):
        parsingMap = ParseMapModel()

        patternModelBFSList = self.BFSForInitializeConditionAction(patternModel)

        i = len(patternModelBFSList) - 1

        while i > -1:
            for con in patternModelBFSList[i].cons:
                if not con.execute(patternModelBFSList[i], parsingMap):
                    logging.error("[ERROR] constrainPattern error! in wordStr:{}, entityType:{}".format(patternModelBFSList[i].wordStr, patternModelBFSList[i].entityType))
                    return None
            i -= 1

        return parsingMap



    def BFSForInitializeConditionAction(self, root):
        patternModelBFSList = []
        patternModelQueue = []
        patternModelQueue.append(root)
        while len(patternModelQueue) > 0:
            extractionModel = patternModelQueue.pop()
            patternModelBFSList.append(extractionModel)
            for aWord in extractionModel.subWordModels:
                if isinstance(aWord, PatternModel):
                    tmp = aWord
                    patternModelQueue.append(tmp)

        return patternModelBFSList


puma_extractPattern = ExtractPattern()
puma_parsePattern = ParsePattern()
puma_extractToMaxList = ExtractToMaxList()









