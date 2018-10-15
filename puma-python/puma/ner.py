

from .config import puma_config
from .config import puma_configNLP

from .scene import *

import re



class Feature:

    @staticmethod
    def generate(i, wordModelMaximize, sceceList, entityTypeList):

        data = None

        if SceneBase_Date.sceneName in map(lambda x:x.sceneName, sceceList[i]):

            data = [0] * 7

            sceneSet = sceceList[i]

            dateNum = 0

            for j in range(i):
                if SceneBase_Date in map(lambda x:x.sceneName, sceceList[j]) >= 0:
                    dateNum += 1

            sceneNum = 0
            for scene in sceneSet:
                if not scene.sceneName == SceneBase_Date.sceneName:
                    tempNum = 0
                    for j in range(i):
                        if scene in sceceList[j]:
                            tempNum += 1

                    sceneNum += tempNum

            data[0] = 1 if i == 1 else 0
            data[1] = 1 if i == len(sceceList) - 2 else 0
            data[2] = 1 if dateNum > 0 else 0
            data[3] = 1 if sceneNum > 0 else 0
            data[4] = 1 if SceneBase_Number.sceneName in map(lambda x:x.sceneName,sceneSet) else 0
            data[5] = 1
            if (data[4] == 1):
                try:
                    data[6] = float(wordModelMaximize[i][0].wordStr)
                except Exception as e:
                    data[6] = 0
            else:
                data[6] = 0

        return data

    @staticmethod
    def judge(data):
        if (data[6] > 2200 and data[6] < 9999) or (data[6] < 1999 and data[6] >= 20):
            return 0
        else:
            return 1



class Recognize:

    def __init__(self):

        pass

    def RecognizeEntityType(self, queryModel):

        entityTypeMaximize = []
        sceneList = []
        entityTypeList = []

        for wordModels in queryModel.wordModelMaximize:
            scenes = []
            entityTypes = []
            for aWordModel in wordModels:
                scenes.append(aWordModel.scene)
                entityTypes.append(aWordModel.entityType)

            sceneList.append(scenes)
            entityTypeList.append(entityTypes)

        for i in range(len(queryModel.wordModelMaximize)):

            entityTypes = []

            if SceneBase_Date.sceneName in map(lambda x:x.sceneName, sceneList[i]):

                data = Feature.generate(i, queryModel.wordModelMaximize, sceneList, entityTypeList)

                for aWordModel in queryModel.wordModelMaximize[i]:

                    if Feature.judge(data) == 1:
                        if not aWordModel.scene.sceneName == SceneBase_Number.sceneName:
                            entityTypes.append(aWordModel.entityType)
                    else:
                        if not aWordModel.scene.sceneName == SceneBase_Date.sceneName:
                            entityTypes.append(aWordModel.entityType)

                if "date_relative_range_extraction" in entityTypes and "date_calendar_range_extraction" in entityTypes:
                    wordStr = queryModel.wordModelMaximize[i][0].wordStr
                    if wordStr.find("年") >= 0:

                        matcher = re.match("\d+", wordStr)

                        if matcher:
                            years = int(matcher.group())
                            if years > 10:
                                entityTypes.remove("date_relative_range_extraction")
                            else:
                                entityTypes.remove("date_calendar_range_extraction")
                    elif wordStr.find("月") >= 0:
                        entityTypes.remove("date_relative_range_extraction")
                    elif wordStr.find("日") >= 0 or wordStr.find("天") >= 0 or wordStr.find("号") >= 0:
                        entityTypes.remove("date_calendar_range_extraction")
            else:
                entityTypes = entityTypeList[i]

            entityTypeMaximize.append(entityTypes)

        queryModel.wordModelMaximize = self.regroupMaximize(queryModel.wordModelMaximize, entityTypeMaximize)




    def regroupMaximize(self, wordModelMaximize, entityTypeMaximize):
        assert len(wordModelMaximize) == len(entityTypeMaximize)
        for i in range(len(wordModelMaximize)):
            entityTypes = entityTypeMaximize[i]

            j = len(wordModelMaximize[i]) - 1
            while j > -1:
                if not wordModelMaximize[i][j].entityType in entityTypes:
                    wordModelMaximize[i].pop(j)
                j -= 1

        return wordModelMaximize


puma_recognize = Recognize()





