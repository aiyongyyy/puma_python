import re

from .model import *

unitMap = {
"个" : 1,
"十" : 10,
"百" : 100,
"千" : 1000,
"万" : 10000,
"亿" : 100000000,
}

numMap = {
"零" : 0.0,
"一" : 1.0,
"二" : 2.0,
"三" : 3.0,
"四" : 4.0,
"五" : 5.0,
"六" : 6.0,
"七" : 7.0,
"八" : 8.0,
"九" : 9.0,
"两" : 2.0,
"半" : 0.5,
}

class EntityAnnotator:

    def __init__(self):
        pass


class Entity:

    def __init__(self):
        pass

    def entityTag(self, queryModel):
        pass


class EntityAlphabet(Entity):

    def __init__(self):
        self.pattern = re.compile(r'[a-zA-Z]+')

    def entityTag(self, queryModel):
        result = self.pattern.finditer(queryModel.querySentence)
        for matcher in result:
            aToken = TokenModel()
            aToken.wordStr = matcher.group()
            aToken.entityType = "alphabet"
            aToken.scene = SceneBase_Constant
            queryModel.addWordModel(aToken, matcher.start())

        return True

class EntityArabicNumber(Entity):

    def __init__(self):
        self.pattern = re.compile(r'[0-9]+(\.[0-9]+)?(%|％)?')
        self.patternNeg = re.compile(r'-[0-9]+(\.[0-9]+)?(%|％)?')

    def entityTag(self, queryModel):
        result = self.pattern.finditer(queryModel.querySentence)
        for matcher in result:
            num = matcher.group()
            aToken = TokenModel()
            aToken.wordStr = num
            aToken.entityType = "arabic_number"
            if num.endswith("%") or num.endswith("％"):
                aToken.actualValue = float(num[0:len(num) - 1]) / 100
            else:
                aToken.actualValue = float(num)
            aToken.scene = SceneBase_Number
            queryModel.addWordModel(aToken, matcher.start())

        resultNeg = self.patternNeg.finditer(queryModel.querySentence)
        for matcher in resultNeg:
            num = matcher.group()
            aToken = TokenModel()
            aToken.wordStr = num
            aToken.entityType = "arabic_number"
            if num.endswith("%") or num.endswith("％"):
                aToken.actualValue = float(num[0:len(num) - 1]) / 100
            else:
                aToken.actualValue = float(num[0:len(num)-1])
            aToken.scene = SceneBase_Number
            queryModel.addWordModel(aToken, matcher.start())

        return True



class EntityChineseNumber(Entity):

    def __init__(self):
        pass

    def entityTag(self, queryModel):
        startPos = -1
        for i in range(len(queryModel.wordModelList)):
            word0 = queryModel.getWordModelByEntityType("arabic_number", i)
            if not word0 is None:
                i = word0.endPos - 1
                continue

            word1 = queryModel.getWordModelByEntityType("number_chinese", i)
            word2 = queryModel.getWordModelByEntityType("number_chinese_bit", i)
            if not word1 and not word2:
                if startPos == -1:
                    continue
                else:
                    aToken = TokenModel()
                    aToken.wordStr = queryModel.querySentence[startPos:i]
                    aToken.entityType = "arabic_number"
                    aToken.actualValue = float(self.chineseToArabic(aToken.wordStr))
                    aToken.scene = SceneBase_Number
                    queryModel.addWordModel(aToken, startPos)
                    startPos = -1
            else:
                if startPos == -1 and word1:
                    startPos = i
                else:
                    continue

        if startPos != -1:
            aToken = TokenModel()
            aToken.wordStr = queryModel.querySentence[startPos:]
            aToken.entityType = "arabic_number"
            aToken.actualValue = float(self.chineseToArabic(aToken.wordStr))
            aToken.scene = SceneBase_Number
            queryModel.addWordModel(aToken, startPos)

        return True


    @staticmethod
    def chineseToArabic(chineseNumber):
        try:
            dataMap = {}
            multiNumList = []

            tempNum = 0
            for i in range(len(chineseNumber)):
                bit = chineseNumber[i]

                isExist = False

                if (chineseNumber.find('亿',i) >= 0 or chineseNumber.find('万',i) >= 0) and chineseNumber[i] != '亿' and chineseNumber[i] != '万':
                    isExist = True

                if bit in numMap:
                    if i != len(chineseNumber) - 1:
                        tempNum = tempNum + numMap[bit]
                    else:
                        dataMap["个"] = float(numMap[bit])
                        tempNum = 0
                elif bit == '亿':
                    if i - 1 >=0 and chineseNumber[i-1] == '万':
                        dataValue = dataMap["万"]
                        if dataValue and dataValue > 0:
                            dataMap["万"] = dataValue * unitMap[bit]
                        continue
                    if tempNum != 0:
                        multiNumList.append(tempNum)

                    sum = 0
                    for num in multiNumList:
                        sum += num

                    multiNumList.clear()
                    dataMap["亿"] = sum
                    tempNum = 0
                elif bit == '万':
                    if tempNum != 0:
                        multiNumList.append(tempNum)

                    sum = 0
                    for num in multiNumList:
                        sum += num

                    multiNumList.clear()
                    dataMap["万"] = sum
                    tempNum = 0
                elif bit == '千' and tempNum > 0:
                    if isExist:
                        multiNumList.append(tempNum * unitMap[bit])
                        tempNum = 0
                    else:
                        dataMap["千"] = tempNum
                        tempNum = 0
                elif bit == '百' and tempNum > 0:
                    if isExist:
                        multiNumList.append(tempNum * unitMap[bit])
                        tempNum = 0
                    else:
                        dataMap["百"] = tempNum
                        tempNum = 0
                elif bit == '十':
                    if isExist:
                        if tempNum != 0:
                            multiNumList.append(tempNum * unitMap[bit])
                            tempNum = 0
                        else:
                            tempNum = 1 * unitMap[bit]
                    else:
                        if tempNum != 0:
                            dataMap["十"] = tempNum
                        else:
                            dataMap["十"] = 1.0
                        tempNum = 0
                elif bit == '个':
                    if isExist:
                        if tempNum != 0:
                            multiNumList.append(tempNum * unitMap[bit])
                            tempNum = 0
                        else:
                            tempNum = 1 * unitMap[bit]
                    else:
                        if tempNum != 0:
                            dataMap["个"] = tempNum
                        else:
                            dataMap["个"] = 1.0
                        tempNum = 0

            sum = 0.0
            keys = dataMap.keys()
            for key in keys:
                unitValue = unitMap[key]
                dataValue = dataMap[key]
                sum += unitValue * dataValue

            return sum

        except Exception as e:
            return 0.0




class EntityCoChineseArabicNumber(Entity):

    def entityTag(self, queryModel):
        for i in range(len(queryModel.wordModelList)):
            token1 = queryModel.getWordModelByEntityType("arabic_number", i)
            if token1 is None:
                continue
            token2 = queryModel.getWordModelByEntityType("number_chinese_bit", token1.endPos)
            if token2:
                token1.wordStr = token1.wordStr + token2.wordStr
                token1.endPos = token1.endPos + len(token2.wordStr)
                token1.actualValue = float(token1.actualValue) * EntityChineseNumber.chineseToArabic("一" + token2.wordStr)

        return True

class EntityCoChinesePercentNumber(Entity):

    def entityTag(self, queryModel):
        for i in range(len(queryModel.wordModelList)):
            token = queryModel.getWordModelByEntityType("arabic_number", i)
            if not token:
                continue
            i = token.endPos
            if i < len(queryModel.wordModelList):
                for wordModel in queryModel.wordModelList[i]:
                    if wordModel.wordStr == "百分点" or wordModel.wordStr == "百分数":
                        token.wordStr = token.wordStr + wordModel.wordStr
                        token.endPos = token.endPos + len(wordModel.wordStr)
                        token.actualValue = float(token.actualValue) * 0.01
                    elif wordModel.wordStr == "基点":
                        token.wordStr = token.wordStr + wordModel.wordStr
                        token.endPos = token.endPos + len(wordModel.wordStr)
                        token.actualValue = float(token.actualValue) * 0.0001

            tokenPercent = queryModel.getWordModelByEntityType("number_chinese_percent", token.startPos - 3)
            if not tokenPercent is None:
                aToken = TokenModel()
                aToken.wordStr = tokenPercent.wordStr + token.wordStr
                aToken.entityType = "arabic_number"
                aToken.startPos = tokenPercent.startPos
                aToken.endPos = token.endPos
                aToken.actualValue = float(token.actualValue) * 0.01
                aToken.scene = SceneBase_Number
                queryModel.addWordModel(aToken, tokenPercent.startPos)

            tokenUnit = queryModel.getWordModelByEntityType("number_unit", i)
            if tokenUnit:
                token.wordStr = token.wordStr + tokenUnit.wordStr
                token.endPos = token.endPos + len(tokenUnit.wordStr)

        return True


class EntityDate(Entity):

    def __init__(self):

        self.patternyyyyMMddNumber = re.compile(
            "([12][0-9]{3})([01][0-9])([0-3][0-9])|([12][0-9]{3})([01][0-9])|([01][0-9])([0-3][0-9])")
        self.patternyyyyMMddBlank = re.compile(
            "([12][0-9]{3}|[0-9]{2})(/|\\.|-)(([1][0-2])|([0]?[1-9]))(/|\\.|-)(([3][01])|([0-2]?[0-9]))")
        self.patternyyyyMMdd = re.compile(
            "([12][0-9]{3}|[0-9]{2})(年度|年)(([1][0-2])|([0]?[1-9]))(月)(([3][01])|([0-2]?[0-9]))(日|天|号)")
        self.patternyyyyMM = re.compile("([12][0-9]{3}|[0-9]{2})(年度|年)(([1][0-2])|([0]?[1-9]))(月份|月)")
        self.patternMMdd = re.compile(
            "(([01]?[0-9])(月)(([3][01])|([0-2]?[0-9]))(日|天|号))|((([1][0-2])|([0]?[1-9]))(/|\\.|-)(([3][01])|([1-2][0-9])|([0]?[1-9])))")
        self.patternyyyy = re.compile("([12][0-9]{3}(年度|年)?)|([0-9]{2}(年度|年))")
        self.patternMM = re.compile("(([1][0-2])|([0]?[1-9]))(月份|月)")
        self.patterndd = re.compile("(([3][01])|([0-2]?[0-9]))(号)") # 去除15号基金的badcase

        self.replaceTag = "/|\\.|-|年度|月份|年|月|日|天|号"
        self.replaceTag1 = "/|\\.|-"

    def entityTag(self, queryModel):
        dateIndex = set()

        start = -1
        result = self.patternyyyyMMddNumber.search(queryModel.querySentence, start)
        while result:
            start = result.start()
            if result.start() in dateIndex:
                start = start+1
                result = self.patternyyyyMMddNumber.search(queryModel.querySentence, start)
                continue

            aToken = TokenModel()
            aToken.wordStr = result.group()
            date = aToken.wordStr
            if len(date) == 4:
                date = date[0:4] + "日" + date[4:]
                date = date[0:2] + "月" + date[2:]
                aToken.entityType = "date_calendar_normal_day"
            elif len(date) == 6:
                date = date[0:6] + "月" + date[6:]
                date = date[0:4] + "年" + date[4:]
                aToken.entityType = "date_calendar_normal_month"
                date += "1日"
            elif len(date) == 8:
                date = date[0:8] + "日" + date[8:]
                date = date[0:6] + "月" + date[6:]
                date = date[0:4] + "年" + date[4:]
                aToken.entityType = "date_calendar_normal_day"
            aToken.actualValue = date
            aToken.scene = SceneBase_Date
            valid = queryModel.addWordModel(aToken, result.start())
            if valid:
                for i in range(result.start(), result.start() + len(aToken.wordStr)):
                    dateIndex.add(i)

            start += 1
            result = self.patternyyyyMMddNumber.search(queryModel.querySentence, start)


        start = -1
        result = self.patternyyyyMMdd.search(queryModel.querySentence, start)
        while result:
            start = result.start()
            if result.start() in dateIndex:
                start = start+1
                result = self.patternyyyyMMdd.search(queryModel.querySentence, start)
                continue

            aToken = TokenModel()
            aToken.wordStr = result.group()
            aToken.entityType = "date_calendar_normal_day"
            date = ""
            seg = re.split(self.replaceTag, aToken.wordStr)
            seg0 = int(seg[0])
            if seg0 < 100 and seg0 > 50:
                date += "19"
            elif seg0 < 50:
                date += "20"
            date += seg[0]
            date += "年"
            date += seg[1]
            date += "月"
            date += seg[2]
            date += "日"
            aToken.actualValue = date
            aToken.scene = SceneBase_Date
            valid = queryModel.addWordModel(aToken, result.start())
            if valid:
                for i in range(result.start(), result.start()+len(aToken.wordStr)):
                    dateIndex.add(i)

            start += 1
            result = self.patternyyyyMMdd.search(queryModel.querySentence, start)


        start = -1
        result = self.patternyyyyMMddBlank.search(queryModel.querySentence, start)
        while result:
            start = result.start()
            if result.start() in dateIndex:
                start = start+1
                result = self.patternyyyyMMddBlank.search(queryModel.querySentence, start)
                continue

            aToken = TokenModel()
            aToken.wordStr = result.group()
            aToken.entityType = "date_calendar_normal_day"

            count = 0
            for replace in self.replaceTag.split("|"):
                if aToken.wordStr.find(replace) >= 0:
                    count += 1

            if count > 1:
                start = start+1
                result = self.patternyyyyMMddBlank.search(queryModel.querySentence, start)
                continue

            date = ""
            seg = re.split(self.replaceTag, aToken.wordStr)
            seg0 = int(seg[0])
            if seg0 < 100 and seg0 > 50:
                date += "19"
            elif seg0 < 50:
                date += "20"
            date += seg[0]
            date += "年"
            date += seg[1]
            date += "月"
            date += seg[2]
            date += "日"
            aToken.actualValue = date
            aToken.scene = SceneBase_Date
            valid = queryModel.addWordModel(aToken, result.start())
            if valid:
                for i in range(result.start(), result.start() + len(aToken.wordStr)):
                    dateIndex.add(i)

            start += 1
            result = self.patternyyyyMMddBlank.search(queryModel.querySentence, start)

        start = -1
        result = self.patternyyyyMM.search(queryModel.querySentence, start)
        while result:
            start = result.start()
            if result.start() in dateIndex:
                start = start+1
                result = self.patternyyyyMM.search(queryModel.querySentence, start)
                continue

            aToken = TokenModel()
            aToken.wordStr = result.group()
            aToken.entityType = "date_calendar_normal_month"
            date = ""
            seg = re.split(self.replaceTag, aToken.wordStr)
            seg0 = int(seg[0])
            if seg0<100 and seg0>50:
                date += "19"
            elif seg0<50:
                date += "20"
            date += seg[0]
            date += "年"
            date += seg[1]
            date += "月"
            date += "1日"
            aToken.actualValue = date
            aToken.scene = SceneBase_Date
            valid = queryModel.addWordModel(aToken, result.start())
            if valid:
                for i in range(result.start(), result.start() + len(aToken.wordStr)):
                    dateIndex.add(i)

            start = start + 1
            result = self.patternyyyyMM.search(queryModel.querySentence, start)

        start = -1
        result = self.patternMMdd.search(queryModel.querySentence, start)
        while result:
            start = result.start()
            if result.start() in dateIndex:
                start = start+1
                result = self.patternMMdd.search(queryModel.querySentence, start)
                continue

            aToken = TokenModel()
            aToken.wordStr = result.group()
            aToken.entityType = "date_calendar_normal_day"
            date = ""
            seg = re.split(self.replaceTag, aToken.wordStr)
            date += seg[0]
            date += "月"
            date += seg[1]
            date += "日"
            aToken.actualValue = date
            aToken.scene = SceneBase_Date
            valid = queryModel.addWordModel(aToken, result.start())
            if valid:
                for i in range(result.start(), result.start() + len(aToken.wordStr)):
                    dateIndex.add(i)

            start = start + 1
            result = self.patternMMdd.search(queryModel.querySentence, start)

        start = -1
        result = self.patternyyyy.search(queryModel.querySentence, start)
        while result:
            start = result.start()
            if result.start() in dateIndex:
                start = start+1
                result = self.patternyyyy.search(queryModel.querySentence, start)
                continue

            aToken = TokenModel()
            aToken.wordStr = result.group()
            aToken.entityType = "date_calendar_normal_year"
            date = ""
            seg = re.split(self.replaceTag, aToken.wordStr)
            seg0 = int(seg[0])
            if seg0<100 and seg0>50:
                date += "19"
            elif seg0<50:
                date += "20"
            date += seg[0]
            date += "年"
            date += "1月1日";
            aToken.actualValue = date
            aToken.scene = SceneBase_Date
            valid = queryModel.addWordModel(aToken, result.start())
            if valid:
                for i in range(result.start(), result.start() + len(aToken.wordStr)):
                    dateIndex.add(i)

            start = start + 1
            result = self.patternyyyy.search(queryModel.querySentence, start)


        start = -1
        result = self.patternMM.search(queryModel.querySentence, start)
        while result:
            start = result.start()
            if result.start() in dateIndex:
                start = start+1
                result = self.patternMM.search(queryModel.querySentence, start)
                continue

            aToken = TokenModel()
            aToken.wordStr = result.group()
            aToken.entityType = "date_calendar_normal_month"
            date = ""
            seg = re.split(self.replaceTag, aToken.wordStr)
            date += seg[0]
            date += "月"
            date += "1日"
            aToken.actualValue = date
            aToken.scene = SceneBase_Date
            valid = queryModel.addWordModel(aToken, result.start())
            if valid:
                for i in range(result.start(), result.start() + len(aToken.wordStr)):
                    dateIndex.add(i)

            start = start + 1
            result = self.patternMM.search(queryModel.querySentence, start)

        start = -1
        result = self.patterndd.search(queryModel.querySentence, start)
        while result:
            start = result.start()
            if result.start() in dateIndex:
                start = start+1
                result = self.patterndd.search(queryModel.querySentence, start)
                continue

            aToken = TokenModel()
            aToken.wordStr = result.group()
            aToken.entityType = "date_calendar_normal_day"
            date = ""
            seg = re.split(self.replaceTag, aToken.wordStr)
            date += seg[0]
            date += "日"
            aToken.actualValue = date
            aToken.scene = SceneBase_Date
            valid = queryModel.addWordModel(aToken, result.start())
            if valid:
                for i in range(result.start(), result.start() + len(aToken.wordStr)):
                    dateIndex.add(i)

            start = start + 1
            result = self.patterndd.search(queryModel.querySentence, start)

        yearFront = None
        for index in range(len(queryModel.wordModelList)):
            year = queryModel.getWordModelByEntityType("date_calendar_normal_year", index)

            if year:
                yearFront = year

            q1 = queryModel.getWordModelByEntityType("date_ql", index)
            if q1:
                self.addQuat(queryModel, yearFront, q1, "1月1日", "date_calendar_normal_quat", dateIndex)

            q2 = queryModel.getWordModelByEntityType("date_q2", index)
            if q2:
                self.addQuat(queryModel, yearFront, q2, "4月1日", "date_calendar_normal_quat", dateIndex)

            q3 = queryModel.getWordModelByEntityType("date_q3", index)
            if q3:
                self.addQuat(queryModel, yearFront, q3, "7月1日", "date_calendar_normal_quat", dateIndex)

            q4 = queryModel.getWordModelByEntityType("date_q4", index)
            if q4:
                self.addQuat(queryModel, yearFront, q4, "10月1日", "date_calendar_normal_quat", dateIndex)

            q12 = queryModel.getWordModelByEntityType("date_q12", index)
            if q12:
                self.addQuat(queryModel, yearFront, q12, "1月1日", "date_calendar_normal_halfyear", dateIndex)

            q34 = queryModel.getWordModelByEntityType("date_q34", index)
            if q34:
                self.addQuat(queryModel, yearFront, q34, "7月1日", "date_calendar_normal_halfyear", dateIndex)

        return True



    def addQuat(self, queryModel, yearFront, q, day, entityType, dateIndex):
        if q.startPos in dateIndex:
            return False
        valid = False
        if yearFront and q.startPos == yearFront.endPos:
            yearFront.wordStr = yearFront.wordStr + q.wordStr
            yearFront.endPos = q.endPos
            yearFront.entityType = entityType
            yearFront.actualValue = yearFront.actualValue.split("年")[0] + "年" + day
            valid = True
        else:
            aToken = TokenModel()
            aToken.wordStr = q.wordStr
            aToken.entityType = entityType
            aToken.actualValue = day
            aToken.scene = SceneBase_Date
            valid = queryModel.getWordModelByEntityType(aToken, q.startPos)

        if valid:
            for i in range(q.startPos, q.startPos + len(q.wordStr)):
                dateIndex.add(i)

        return True




class EntityScientificNumber(Entity):

    def __init__(self):
        self.pattern = re.compile("[0-9]+(\\.[0-9]+)?(E|e)[0-9]+")
        self.patternNeg = re.compile("-[0-9]+(\\.[0-9]+)?(E|e)[0-9]+")

    def entityTag(self, queryModel):

        result = self.pattern.finditer(queryModel.querySentence)

        for matcher in result:
            num = matcher.group()
            aToken = TokenModel()
            aToken.wordStr = num
            aToken.entityType = "arabic number"
            aToken.actualValue = float(num)
            aToken.scene = SceneBase_Number
            queryModel.addWordModel(aToken, matcher.start())

        result = self.patternNeg.finditer(queryModel.querySentence)

        for matcher in result:
            num = matcher.group()
            aToken = TokenModel()
            aToken.wordStr = num
            aToken.entityType = "arabic number"
            aToken.actualValue = float(num)
            aToken.scene = SceneBase_Number
            queryModel.addWordModel(aToken, matcher.start())

        return True

class EntityNotation(Entity):

    def __init__(self):
        self.patternBook = re.compile("《.*?》")
        self.patternQuotation = re.compile("“.*?”")
        self.patternParentheses = re.compile("（.*?）")
        self.patternList = [self.patternBook, self.patternQuotation, self.patternParentheses]


    def entityTag(self, queryModel):
        for pattern in self.patternList:
            result = pattern.finditer(queryModel.querySentence)

            for matcher in result:
                aToken = TokenModel()
                aToken.wordStr = matcher.group()
                aToken.entityType = "notation"
                aToken.scene = SceneBase_Constant
                queryModel.addWordModel(aToken, matcher.start())

        return True





class EntityProcess:

    def __init__(self):
        self.entityAlphabet = EntityAlphabet()
        self.entityArabicNumber = EntityArabicNumber()
        self.entityScientificNumber = EntityScientificNumber()
        self.entityCoChineseArabicNumber = EntityCoChineseArabicNumber()
        self.entityChineseNumber = EntityChineseNumber()
        self.entityCoChinesePercentNumber = EntityCoChinesePercentNumber()
        self.entityNotation = EntityNotation()
        self.entityDate = EntityDate()


    def EntityRecognition(self, queryModel):
        alphabet = self.entityAlphabet.entityTag(queryModel)
        arbicNumber = self.entityArabicNumber.entityTag(queryModel)
        scientificNumber = self.entityScientificNumber.entityTag(queryModel)
        coChineseArabicNumber = self.entityCoChineseArabicNumber.entityTag(queryModel)
        chineseNumber = self.entityChineseNumber.entityTag(queryModel)
        coChinesePercentNumber = self.entityCoChinesePercentNumber.entityTag(queryModel)
        notation = self.entityNotation.entityTag(queryModel)
        date = self.entityDate.entityTag(queryModel)

        return alphabet and arbicNumber and scientificNumber and coChineseArabicNumber and chineseNumber and coChinesePercentNumber and notation and date



puma_entity = EntityProcess()