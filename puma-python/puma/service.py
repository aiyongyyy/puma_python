
from .segment import puma_segment
from .config import puma_config
from .tokenize import puma_tokenize
from .entity import puma_entity
from .ssplit import puma_querySsplit
from .extraction import *
from .ner import *
from .scene import *
from .contraint import *



class AnalysisService:

    def __init__(self):
        pass


    @staticmethod
    def initialize(lst):
        sentence = "".join(lst)
        logging.info("sample sentence: {}".format(sentence))

        queryModel = QueryModel(sentence)
        puma_segment.initialize(lst)
        puma_segment.segmentQuery(queryModel)

        return queryModel





    @staticmethod
    def annotate(queryModel):

        # if puma_config.DICT_NER_OPEN==1:          not need now
        #     NER.getInstance().NerQuery(queryModel);
        puma_tokenize.TokenizeQuery(queryModel)
        puma_entity.EntityRecognition(queryModel)

        puma_querySsplit.SsplitQueryBySymbol(queryModel, ["。"])

        for aQuery in queryModel.ssplitQueryModel:

            puma_extractPattern.ExtractQuery(aQuery)

            puma_extractToMaxList.toMaxList(aQuery)


        queryModel.mergeSsplitQueryModel()
        puma_recognize.RecognizeEntityType(queryModel)


    @staticmethod
    def parsing(queryModel):
        for i in range(len(queryModel.wordModelMaximize)):
            wordModels = queryModel.wordModelMaximize[i]
            wordModelsAppend = []
            for wordModel in wordModels:
                if isinstance(wordModel, PatternModel):
                    aPatternModel = wordModel

                    if aPatternModel.scene.sceneName == SceneBase_Date.sceneName:
                        date = puma_dateConstrain.getDateConstraint(aPatternModel)
                        if not date is None:
                            aParseModel = ParseModel()
                            aParseModel.wordStr = aPatternModel.wordStr
                            aParseModel.entityType = aPatternModel.entityType
                            aParseModel.scene = aPatternModel.scene
                            aParseModel.parseMap["orig"] = aPatternModel.wordStr
                            aParseModel.parseMap["date"] = date
                            wordModelsAppend.append(aParseModel)

                    if aPatternModel.scene.sceneName == SceneBase_Number.sceneName:
                        parseMapModel = puma_parsePattern.ParseQueryByPattern(aPatternModel)
                        parsingMap = parseMapModel.state_parsing_map
                        if len(parsingMap) > 0:
                            aParseModel = ParseModel()
                            aParseModel.wordStr = aPatternModel.wordStr
                            aParseModel.entityType = aPatternModel.entityType
                            aParseModel.scene = aPatternModel.scene
                            aParseModel.parseMap["orig"] = aPatternModel.wordStr
                            for entry in parsingMap["number"]:
                                aParseModel.parseMap[entry] = parsingMap["number"][entry]

                            wordModelsAppend.append(aParseModel)

            wordModels.extend(wordModelsAppend)


    @staticmethod
    def output(queryModel):
        ParseModelList = []
        for wordModels in queryModel.wordModelMaximize:
            newModels = ExtractFilter.selectExtractionParse(wordModels, lambda x : True)
            for newModel in newModels:
                ParseModelList.append(newModel)

        parsingMapList = []
        for parseModel in ParseModelList:
            map = {}
            map[parseModel.scene.getSceneName()] = parseModel.parseMap
            parsingMapList.append(map)

        for parsingMap in parsingMapList:
            print(parsingMap)

        return parsingMapList





    @staticmethod
    def getDateFeatureForQuestion(cuts):
        question = "".join(cuts)
        original = question
        retMap = {}
        words = []
        datewords = []
        event_date = []

        try:
            queryModel = AnalysisService.initialize(cuts)
            AnalysisService.annotate(queryModel)
            AnalysisService.parsing(queryModel)

            result = AnalysisService.output(queryModel)

            for e in result:
                try:
                    s = e["date"]
                    time = s["date"]
                    time = time.replace("-", "")
                    time = time.replace("[ ,", "[20000101,")
                    time = time.replace(", )", ",20200101)")

                    begin = datetime.datetime.strptime(time[1:9], "%Y%m%d")
                    end = datetime.datetime.strptime(time[10:18], "%Y%m%d")

                    if datetime.datetime.now() < begin:
                        begin = datetime.datetime(year=begin.year-1, month=begin.month, day=begin.day)
                        end = datetime.datetime(year=end.year - 1, month=end.month, day=end.day)

                    sdf = "%Y%m%d"
                    endTime = end.strftime(sdf)
                    beginTime = begin.strftime(sdf)

                    time = beginTime + "-" + endTime

                    orig = s["orig"]

                    if orig.find("季度") >= 0:
                        question = question.replace(orig, "DATE季度")
                    if orig.find("季报") >= 0:
                        question = question.replace(orig, "DATE季报")
                    question = question.replace(orig, "DATE")
                    words.append(orig)
                    datewords.append(time)

                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)

        if question.find("DATE度") >= 0 and original.find("年度") >= 0:
            question = question.replace("DATE度", "DATE年度")

        findYear = False
        findMonth = False

        if question.find("DATEDATE") >= 0 and len(words) == 2:
            for e in words:
                if len(e) == 2 and e.find("年") >= 0:
                    findYear = True
                if not e.find("年") >= 0:
                    findMonth = True

            if findMonth and findYear:
                question = question.replace("DATEDATE", "DATE")
                year1 = datewords[0][0:4]
                year2 = datewords[1][0:4]
                datewords[1] = datewords[1].replace(year2, year1)
                datewords.pop(0)

        retMap["dateQuestion"] = question
        retMap["dateWords"] = datewords
        retMap["words"] = words

        return retMap






    @staticmethod
    def getDateRangeFeatureForQuestion(cutQuestion):

        strArray = cutQuestion.split(",")

        cuts = []

        for str in strArray:
            cuts.append(str)

        question = "".join(cuts)

        dateMap = AnalysisService.getDateFeatureForQuestion(cuts)

        if dateMap["dateWords"] is None or len(dateMap["dateWords"]) == 0:
            return dateMap["dateQuestion"]

        dateString = dateMap["dateWords"][0]
        splits = dateString.split("-")

        if not splits[0] == splits[1]:
            dateRange = dateMap["dateQuestion"].replace("DATE", "DATERANGE")
            dateMap["dateQuestion"] = dateRange

        retStr = ""
        retStr += dateMap["dateQuestion"] + "!@#$%"
        retStr += ",".join(dateMap["words"]) + "!@#$%"
        retStr += ",".join(dateMap["dateWords"])

        return retStr





