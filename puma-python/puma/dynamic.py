from .utils.constantsdefine import *
from .state import *
from .model import *

import logging

class DynamicJava:

    def f0(self, v):
        return v[0] is not None

    def f1(self, v):
        return v[0]

    def f2(self, v):
        return v[0] is not None

    def f3(self, v):
        return v[0]

    def f4(self, v):
        return v[0] is not None

    def f5(self, v):
        return v[0]

    def f6(self, v):
        return v[0] is not None

    def f7(self, v):
        return v[0]

    def f8(self, v):
        return v[0] is not None

    def f9(self, v):
        return v[0]

    def f10(self, v):
        return True

    def f11(self, v):
        return v[0]

    def f12(self, v):
        return v[0] is not None

    def f13(self, v):
        return "年"

    def f14(self, v):
        return v[0] is not None

    def f15(self, v):
        return "月"

    def f16(self, v):
        return v[0] is not None

    def f17(self, v):
        return "周"

    def f18(self, v):
        return v[0] is not None

    def f19(self, v):
        return "日"

    def f20(self, v):
        return v[0] is not None

    def f21(self, v):
        return "季度"

    def f22(self, v):
        return v[0] is not None or v[1] is not None

    def f23(self, v):
        return "before"

    def f24(self, v):
        return v[0] is not None or v[1] is not None

    def f25(self, v):
        return "after"

    def f26(self, v):
        return v[0] is not None or v[1] is not None

    def f27(self, v):
        return "forward"

    def f28(self, v):
        return v[0] is not None or v[1] is not None

    def f29(self, v):
        return "backward"

    def f30(self, v):
        return v[0] is not None

    def f31(self, v):
        return v[0]

    def f32(self, v):
        return v[0] is not None

    def f33(self, v):
        return v[0]

    def f34(self, v):
        return v[0] is not None

    def f35(self, v):
        return v[0]

    def f36(self, v):
        return v[0] is not None

    def f37(self, v):
        return v[0]

    def f38(self, v):
        return v[0] is not None

    def f39(self, v):
        return v[0]

    def f40(self, v):
        return v[0] is not None

    def f41(self, v):
        return v[0]

    def f42(self, v):
        return v[0] is not None

    def f43(self, v):
        return v[0]

    def f44(self, v):
        return v[0] is not None

    def f45(self, v):
        return v[0]

    def f46(self, v):
        return v[0] is not None

    def f47(self, v):
        return v[0]

    def f48(self, v):
        return v[0] is not None

    def f49(self, v):
        return v[0]

    def f50(self, v):
        return v[0] is not None

    def f51(self, v):
        return v[0]

    def f52(self, v):
        return v[0] is not None

    def f53(self, v):
        return v[0]

    def f54(self, v):
        return v[0] is not None

    def f55(self, v):
        return v[0]

    def f56(self, v):
        return v[0] is not None

    def f57(self, v):
        return v[0]

    def f58(self, v):
        return v[0] is not None

    def f59(self, v):
        return v[0]

    def f60(self, v):
        return v[0] is not None

    def f61(self, v):
        return v[0]

    def f62(self, v):
        return v[0] is not None

    def f63(self, v):
        return v[0]

    def f64(self, v):
        return v[0] is not None

    def f65(self, v):
        return v[0]

    def f66(self, v):
        return v[0] is not None

    def f67(self, v):
        return v[0]

    def f68(self, v):
        return v[0] is not None

    def f69(self, v):
        return v[0]

    def f70(self, v):
        return v[0] is not None

    def f71(self, v):
        return "before"

    def f72(self, v):
        return v[0] is not None

    def f73(self, v):
        return "after"

    def f74(self, v):
        return v[0] is not None

    def f75(self, v):
        return "forward"

    def f76(self, v):
        return v[0] is not None

    def f77(self, v):
        return "backward"

    def f78(self, v):
        return True

    def f79(self, v):
        return v[0]

    def f80(self, v):
        return v[0] is not None

    def f81(self, v):
        return "年"

    def f82(self, v):
        return v[0] is not None

    def f83(self, v):
        return "月"

    def f84(self, v):
        return v[0] is not None

    def f85(self, v):
        return "周"

    def f86(self, v):
        return v[0] is not None

    def f87(self, v):
        return "日"

    def f88(self, v):
        return v[0] is not None

    def f89(self, v):
        return "季度"

    def f90(self, v):
        return True

    def f91(self, v):
        return "forward"

    def f92(self, v):
        return v[0] is not None

    def f93(self, v):
        return v[0]

    def f94(self, v):
        return "(" + str(v[0]) + ", )"

    def f95(self, v):
        return v[0] is not None or v[1] is not None

    def f96(self, v):
        return v[0]

    def f97(self, v):
        return "[" + str(v[0]) + ", )"

    def f98(self, v):
        return v[0] is not None or v[1] is not None

    def f99(self, v):
        return v[0] is not None

    def f100(self, v):
        return "( ," + str(v[0]) + ")"

    def f101(self, v):
        return v[0] is not None or v[1] is not None

    def f102(self, v):
        return v[0]

    def f103(self, v):
        return "( ," + str(v[0]) + "]"

    def f104(self, v):
        return True

    def f105(self, v):
        return v[0]

    def f106(self, v):
        return "[" + str(v[0] * 0.9) + "," + str(v[1] * 1.1) + "]"

    def f107(self, v):
        return v[0] is not None and v[1] is not None

    def f108(self, v):
        return "(" + str(v[0]) + "," + str(v[1]) + ")"

    def f109(self, v):
        return v[0] is not None and v[1] is not None

    def f110(self, v):
        return "(" + str(v[0]) + "," + str(v[1]) + ")"

    def f111(self, v):
        return v[0] is not None and v[1] is not None

    def f112(self, v):
        return "前" + str(v[0])

    def f113(self, v):
        return v[0] is not None and v[1] is not None

    def f114(self, v):
        return "前" + "INFINITY"

    def f115(self, v):
        return v[0] is not None and v[1] is not None

    def f116(self, v):
        return "后" + str(v[0])

    def f117(self, v):
        return v[0] is not None and v[1] is not None

    def f118(self, v):
        return "后" + "INFINITY"

    def f119(self, v):
        return v[0] is None and v[1] is None and v[2] is None and v[3] is None

    def f120(self, v):
        return "!null"

    def f121(self, v):
        return v[0] is not None

    def f122(self, v):
        return v[0]

    def f123(self, v):
        return v[0] is not None

    def f124(self, v):
        return v[0]

    def f125(self, v):
        return v[0] is not None

    def f126(self, v):
        return v[0]

    def f127(self, v):
        return v[0] is not None

    def f128(self, v):
        return v[0]

    def f129(self, v):
        return v[0] is None and v[1] is None and v[2] is None and v[3] is None

    def f130(self, v):
        return "!null"

    def f131(self, v):
        return v[0] is not None

    def f132(self, v):
        return v[0]

    def f133(self, v):
        return v[0] is not None

    def f134(self, v):
        return v[0]

    def f135(self, v):
        return v[0] is not None

    def f136(self, v):
        return v[0]

    def f137(self, v):
        return v[0] is not None

    def f138(self, v):
        return v[0]


puma_dynamicJava = DynamicJava()


class DynamicClass:

    expression_function_name_cnt = 0

    @staticmethod
    def execute(methodName, args_class, args):
        try:
            f = getattr(puma_dynamicJava, methodName)
            return f(args)
        except Exception as e:
            return None

    @staticmethod
    def construct(method):
        print(method)


    @staticmethod
    def getFunctionCount():
        DynamicClass.expression_function_name_cnt += 1
        return DynamicClass.expression_function_name_cnt - 1


class DynamicMethod:

    def __init__(self):

        self.expression = ""

        self.stateModelList = []

        self.this_expression_function_name_cnt = DynamicClass.getFunctionCount()

        self.args_class = []


    def construct(self, scene, expression):

        self.expression = expression
        function_str = ""
        function_str += "public Object " + SYMBOL_FUNCTION_PERFIX + str(self.this_expression_function_name_cnt) + "("

        return_str = ""
        return_str += "return  "

        args_class_list = []
        expression_variable_str = ""

        pos = - 1
        posHead = -1
        posEnd = -1

        pos = 0
        variable_count = 0

        posHead = expression.find(VAR_HEAD)

        if posHead > -1:
            posEnd = expression.find(VAR_END, posHead)

        while posHead > -1 and posEnd > -1 and posEnd > posHead:

            if pos < posHead:
                expression_variable_str = expression[pos:posHead]
                return_str += expression_variable_str

            expression_variable_str = expression[posHead + len(VAR_HEAD):posEnd]
            stateModel = StateModel()
            self.stateModelList.append(stateModel)

            if expression_variable_str.find(TAG_TXT) >=0:
                posTag = expression_variable_str.find(TAG_TXT)
                expression_variable_str = expression_variable_str[posTag + len(TAG_TXT):]
                stateModel.expVarType = ExpVarType.EXP_VAR_HIT_TXT
            elif expression_variable_str.find(TAG_JV) >= 0:
                posTag = expression_variable_str.find(TAG_JV)
                expression_variable_str = expression_variable_str[posTag + len(TAG_JV):]
                stateModel.expVarType = ExpVarType.EXP_VAR_HIT_JV
            elif expression_variable_str.find(TAG_PAT) >= 0:
                posTag = expression_variable_str.find(TAG_PAT)
                expression_variable_str = expression_variable_str[posTag + len(TAG_PAT):]
                stateModel.expVarType = ExpVarType.EXP_VAR_HIT_PAT
            else:
                logging.error("there is no ExpVarType for express {}".format(expression))

            if expression_variable_str.find(TAG_String) >= 0:
                posTag = expression_variable_str.find(TAG_String)
                expression_variable_str = expression_variable_str[posTag + len(TAG_String):]
                stateModel.javaVarType = JavaVarType.Java_Var_String
            elif expression_variable_str.find(TAG_Double) >= 0:
                posTag = expression_variable_str.find(TAG_Double)
                expression_variable_str = expression_variable_str[posTag + len(TAG_Double):]
                stateModel.javaVarType = JavaVarType.Java_Var_Double
            elif expression_variable_str.find(TAG_Boolean) >= 0:
                posTag = expression_variable_str.find(TAG_Boolean)
                expression_variable_str = expression_variable_str[posTag + len(TAG_Boolean):]
                stateModel.javaVarType = JavaVarType.Java_Var_Boolean
            elif expression_variable_str.find(TAG_Object) >= 0:
                posTag = expression_variable_str.find(TAG_Object)
                expression_variable_str = expression_variable_str[posTag + len(TAG_Object):]
                stateModel.javaVarType = JavaVarType.Java_Var_Object
            else:
                logging.warn("there is no JavaVarType for expression {}, will use Object instead".format(expression))
                stateModel.javaVarType = JavaVarType.Java_Var_Object

            stateModel.name = expression_variable_str
            variable_str = SYMBOL_VARIABLE_PERFIX + str(variable_count)
            variable_count += 1
            if stateModel.javaVarType == JavaVarType.Java_Var_Object:
                function_str += "Object"
                args_class_list.append(object)
            elif stateModel.javaVarType == JavaVarType.Java_Var_String:
                function_str += "String "
                args_class_list.append(str)
            elif stateModel.javaVarType == JavaVarType.Java_Var_Double:
                function_str += "Boolean "
                args_class_list.append(bool)

            function_str += variable_str + ","
            return_str += variable_str


            pos = posEnd + len(VAR_END)
            posEnd = -1
            posHead = expression.find(VAR_HEAD, pos)
            if posHead > -1:
                posEnd = expression.find(VAR_END, posHead)

        if pos < len(expression):
            expression_variable_str = expression[pos:len(expression)]
            return_str += expression_variable_str

        if function_str[len(function_str) - 1] == ",":
            function_str = function_str[0:-1]

        function_str += "){"
        return_str += ";}"


        DynamicClass.construct(function_str + return_str)
        self.args_class = args_class_list
        return True

        # DynamicClass.construct(function_str.toString() + return_str.toString());
        # this.args_class = args_class_list.toArray(new
        # Class[args_class_list.size()]);
        # return true;


    def doScript(self, patternModel):

        vec_variables = []

        for stateModel in self.stateModelList:
            if stateModel.expVarType == ExpVarType.EXP_VAR_HIT_TXT:
                addFlag = False
                for aWord in patternModel.subWordModels:
                    if stateModel.name == aWord.entityType:
                        if isinstance(aWord, TokenModel):
                            annotation = aWord
                            if not annotation.actualValue is None:
                                vec_variables.append(aWord.actualValue)
                            else:
                                vec_variables.append(aWord.wordStr)
                        else:
                            vec_variables.append(aWord.wordStr)

                        addFlag = True
                        break

                if not addFlag:
                    vec_variables.append(None)
            elif stateModel.expVarType == ExpVarType.EXP_VAR_HIT_JV:
                arr = stateModel.name.split(SYMBOL_SCENE_BREAK)
                if (len(arr) != 2):
                    logging.error("json var:{} bad format.".format(stateModel.name))
                    vec_variables.append(None)
                    continue

                addFlag = False
                for aWord in patternModel.subWordModels:
                    if arr[0] == aWord.entityType:
                        if isinstance(aWord, TokenModel):
                            annotation = aWord
                            if not annotation.json is None and arr[1] in annotation.json:
                                vec_variables.append(annotation.json[1])
                                addFlag = True
                        break

                if not addFlag:
                    vec_variables.append(None)

            elif stateModel.expVarType == ExpVarType.EXP_VAR_HIT_PAT:
                arr = stateModel.name.split(SYMBOL_SUBEXTRACTION_BREAK)
                if len(arr) != 2:
                    logging.error("json var:{} bad format.".format(stateModel.name))
                    vec_variables.append(None)
                    continue

                addFlag = False
                for aWord in patternModel.subWordModels:
                    if arr[0] == aWord.entityType:
                        if isinstance(aWord, patternModel):
                            if len(arr[1].split(SYMBOL_SCENE_BREAK)) != 2:
                                logging.error("json var:{} bad format.".format(stateModel.name))
                                vec_variables.append(None)
                            else:
                                vec_variables.append(aWord.stateMap[arr[1]])
                                addFlag = True
                        break

                if not addFlag:
                    vec_variables.append(None)

        args = [None]*len(vec_variables)

        for i in range(len(vec_variables)):
            var = vec_variables[i]

            if var is None or isinstance(var, str) or isinstance(var, float) or isinstance(var, bool):
                args[i] = var
            else:
                logging.error("[ERROR] run LuaExpression error for unknow var type. expression: {}, var: {}".format(self.expression, var))
                return None

        result = DynamicClass.execute(SYMBOL_FUNCTION_PERFIX + str(self.this_expression_function_name_cnt), self.args_class, args)

        return result





class Condition(DynamicMethod):

    def __init__(self):
        super(Condition, self).__init__()

    def initializeCondition(self, scene, inputLine):
        return self.construct(scene.getSceneName(), inputLine)


    def judge(self, patternModel):
        result = self.doScript(patternModel)

        if result is None:
            logging.error("[ERROR] run Condition error. in expression: {}".format(self.expression))
        elif isinstance(result, bool):
            return result
        else:
            logging.error("[ERROR] condition return bad result or not boolean!")

        return None



class Action(DynamicMethod):

    def __init__(self):
        super(Action, self).__init__()
        self.vec_target_var_nameWithScene = None

    def initializeAction(self, scene, inputLine):
        pos = inputLine.find("=")
        if pos < 0:
            logging.error("[ERROR] initializeLuaAction error for no =. expression: {}".format(inputLine))
            raise Exception

        target_var_str = inputLine[0 : pos].strip()
        if len(target_var_str) <= (len(VAR_HEAD) + len(VAR_END)) or not target_var_str.startswith(VAR_HEAD) or not target_var_str.endswith(VAR_END):
            logging.error("[ERROR] initializeLuaAction error for no target. expression: {}".format(inputLine))
            raise Exception

        target_var_str = target_var_str[len(VAR_HEAD) : len(target_var_str) - len(VAR_END)]
        if target_var_str in puma_stateCtrl.stateMap:
            self.vec_target_var_nameWithScene = target_var_str
        else:
            logging.error("bad action var:{}".format(target_var_str))
            logging.error("[ERROR] initializeLuaAction error for bad action var. expression: {}".format(inputLine))
            raise Exception

        return self.construct(scene.getSceneName(), inputLine[pos+1:])

    def doAction(self, patternModel):
        result = self.doScript(patternModel)
        if result is None:
            logging.error("[ERROR] run Action error. in expression: {}".format(self.expression))
        else:
            patternModel.stateMap[self.vec_target_var_nameWithScene] = result

        return result



class ConditionAction:

    def __init__(self):
        self.condition = None
        self.v_actions_then = []
        self.v_actions_else = []


    def addActionIf(self, act):
        self.v_actions_then.append(act)

    def addActionElse(self, act):
        self.v_actions_else.append(act)

    def setCondition(self, con):
        self.condition = con

    def execute(self, patternModel, parsingMap):
        judge = self.condition.judge(patternModel)

        if judge is None:
            logging.error("[ERROR] ConditionAction execute error in condition.")
            return False
        elif judge:
            for act in self.v_actions_then:
                result = act.doAction(patternModel)
                if result is None:
                    logging.error("[ERROR] ConditionAction execute error in action then.")
                    return False
                else:
                    parsingMap.setVariableValue(act.vec_target_var_nameWithScene, result)

        else:
            for act in self.v_actions_else:
                result = act.doAction(patternModel)
                if result is None:
                    logging.error("[ERROR] ConditionAction execute error in action else.")
                else:
                    parsingMap.setVariableValue(act.vec_target_var_nameWithScene, result)

        return True

