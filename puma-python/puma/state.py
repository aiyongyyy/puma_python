from .scene import *
from .utils.constantsdefine import *
from .utils.fileutils import *
from .config import *
from .scene import *
import logging

import os

class StateModel:

    def __init__(self):

        self.scene = None
        self.name = None
        self.life_type = None
        self.nameWithScene = None
        self.expVarType = None
        self.javaVarType = None



class StateCtrl:

    def __init__(self):
        self.stateMap = {}
        self.initializeState()

    def initializeState(self):
        for file in puma_config.STATE_FILES.split(","):

            lines = loadListFile(os.path.dirname(os.path.abspath(__file__)) + "/" + puma_config.STATE_PREFIX + file + puma_config.STATE_SUFFIX)

            SCENE = None

            for line_num in range(len(lines)):
                line = lines[line_num].strip()
                if not line or line.startswith(SYMBOL_COMMENT_PERFIX):
                    continue
                elif line.find("SCE:") >= 0:
                    SCENE = puma_scenePool.getSceneByName(line[4:])
                    continue
                elif SCENE is None:
                    logging.error("[ERROR] initializeState error for no scene. in file:{}:{}".format(file, line_num))
                    raise Exception

                vec_str = line.split("\t")
                stateModel = StateModel()
                if len(vec_str) >= 2:
                    stateModel.life_type = VarLifeType(int(vec_str[1]))

                stateModel.name = vec_str[0]
                stateModel.scene = SCENE
                nameWithScene = SCENE.getSceneName() + SYMBOL_SCENE_BREAK + stateModel.name
                stateModel.nameWithScene = nameWithScene
                self.stateMap[nameWithScene] = stateModel

            if len(lines) > 0:
                logging.info("add state {} successfully".format(file))
            else:
                logging.error("add state {} error for find no file".format(file))

        return True

puma_stateCtrl = StateCtrl()
