

class Scene:

    def getSceneName(self):
        pass

    def getSceneClassification(self):
        pass


class SceneBase(Scene):


    def __init__(self, sceneName, sceneClassification):
        self.sceneName = sceneName
        self.sceneClassification = sceneClassification


    def getSceneName(self):
        return self.sceneName

    def getSceneClassification(self):
        return self.sceneClassification



SceneBase_Number = SceneBase("number", 0)
SceneBase_Date = SceneBase("date", 0)
SceneBase_Corporation = SceneBase("corporation", 0)
SceneBase_Segment = SceneBase("segment", -1)
SceneBase_Constant = SceneBase("constant", -1)



class ScenePool:

    def __init__(self):
        self.sceneMap = {}
        self.putSceneByName("number", SceneBase_Number)
        self.putSceneByName("date", SceneBase_Date)
        self.putSceneByName("corporation", SceneBase_Corporation)
        self.putSceneByName("constant", SceneBase_Constant)


    def putSceneByName(self, sceneName, scene):
        self.sceneMap[sceneName] = scene

    def getSceneByName(self, sceneName):
        return self.sceneMap[sceneName]


puma_scenePool = ScenePool()