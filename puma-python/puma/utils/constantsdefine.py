
from enum import Enum

TAG_TXT = "TAG_TXT "
TAG_JV = "TAG_JV "
TAG_PAT = "TAG_PAT "
TAG_Object = "Object "
TAG_String = "String "
TAG_Double = "Double "
TAG_Boolean = "Boolean "
VAR_HEAD = "$["
VAR_END = "]"

SYMBOL_FUNCTION_PERFIX = "f" # 函数名称的前缀符号
SYMBOL_VARIABLE_PERFIX = "v" # 变量名称的前缀符号
SYMBOL_COMMENT_PERFIX = "#" # 文件中注解的前缀符号

SYMBOL_SCENE_BREAK = "::" # 表示场景的分隔符
SYMBOL_ENTITYTYPE_NUMBER_BREAK = "#" # pattern中相同类型EntityType的数字编号
SYMBOL_SUBEXTRACTION_BREAK = "\\." # 取子Extraction的分隔符，要求不同于SYMBOL_Scene1_BREAK

FORMAT_DATETIME_EN = "yyyy-MM-dd kk:mm:ss.SSS"
#FORMAT_DATETIME_YEARMONTHDAY_EN = "yyyy-MM-dd"
FORMAT_DATETIME_YEARMONTHDAY_EN = "%Y-%b-%d"

CONSTRAIN_STARTDATE = "startDate"
CONSTRAIN_ENDDATE = "endDate"
CONSTRAIN_ATDATE = "atDate"

FORMAT_DATE_EN = "%Y-%m-%d"


class STATE_LOAD_FILE(Enum):
    SLF_NORMAL = 1
    SLF_IF = 2
    SLF_IF_OK = 3
    SLF_THEN = 4
    SLF_THEN_OK = 5
    SLF_ELSE = 6
    SLF_ELSE_OK = 7

class VarLifeType(Enum):
    LIFE_APP = 1
    LIFE_SESSION = 2
    LIFE_Scene1 = 3
    LIFE_REQUEST = 4
    LIFE_UNKNOWN = 5

class ExpVarType(Enum):
    EXP_VAR_HIT_TXT = 1
    EXP_VAR_HIT_JV = 2
    EXP_VAR_HIT_PAT = 3

class JavaVarType(Enum):
    Java_Var_Object = 1
    Java_Var_String = 2
    Java_Var_Double = 3
    Java_Var_Boolean = 4


