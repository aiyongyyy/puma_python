# coding:utf8
import os
import configparser



class Config:

    def __init__(self, path):
        self.conf = configparser.ConfigParser()
        self.conf.readfp(open(path))
        self.ENVIRONMENT = self.getConfigValue("env", "dev")
        self.DATA_PATH = self.getConfigValue("path.data", "")

        self.TOKENIZE_FILES = self.getConfigValue("annotation.files")
        self.TOKENIZE_PREFIX = self.getConfigValue("annotation.prefix", "etc/filesample/annotationfiles/")
        self.TOKENIZE_SUFFIX = self.getConfigValue("annotation.suffix", ".dict")
        self.EXTRACT_FILES = self.getConfigValue("extraction.files")
        self.EXTRACT_PREFIX = self.getConfigValue("extraction.prefix", "etc/filesample/extractionfiles/")
        self.EXTRACT_SUFFIX = self.getConfigValue("extraction.suffix", ".rule")
        self.STATE_FILES = self.getConfigValue("state.files")
        self.STATE_PREFIX = self.getConfigValue("state.prefix", "etc/filesample/statefiles/")
        self.STATE_SUFFIX = self.getConfigValue("state.suffix", ".state")

        self.SYNONYM_FILE = self.getConfigValue("synonym.file")
        self.BLACKLIST_FILE = self.getConfigValue("blacklist.file")
        self.ANSJ_DICT_PATH = self.getConfigValue("ansj.dict")

        self.NLP_FILE_PATH = self.getConfigValue("nlp.file")
        self.JAVA_DYNAMIC_COMPILE_PATH = self.getConfigValue("java.compile")

        self.DICT_NER_OPEN = int(self.getConfigValue("dict.ner.open"))
        self.DICT_SQL_OPEN = int(self.getConfigValue("dict.sql.open"))

    def getConfigValue(self, key, defaultValue=""):
        return self.conf.get("config", key) if self.conf.get("config", key) else defaultValue



class ConfigNLP:

    def __init__(self, path):
        self.conf = configparser.ConfigParser()
        self.conf.readfp(open(path))
        self.USER_DEF_DIC_FILE = self.getConfigValue("context.dic.user_def_dic_file")
        self.AMBIGUITY_FILE = self.getConfigValue("context.dic.ambiguity_file")
        self.STOP_WORD_ROOT_PATH = self.getConfigValue("context.dic.user_stopwords")
        self.SINGLE_WORD_ROOT_PATH = self.getConfigValue("context.dic.user_singlewords")
        self.CRF_TEMPLATE_FILE = self.getConfigValue("context.crf.template")
        self.NER_FEATURE_ANNOTATION_RULE_DATA_PATH = self.getConfigValue("context.crf.annotation.rule")
        self.CRF_MODEL_FILE = self.getConfigValue("context.crf.model")
        self.NER_RULE_ANNOTATION_RULE_DATA_PATH = self.getConfigValue("context.annotation.rule")
        self.NER_REGEX_DATE_PATH = self.getConfigValue("regex.date.dict")




    def getConfigValue(self, key, defaultValue=""):
        return self.conf.get("config", key) if self.conf.get("config", key) else defaultValue

puma_config = Config(os.path.dirname(os.path.abspath(__file__)) + "/" + "basenlp.properties")

puma_configNLP = ConfigNLP(os.path.dirname(os.path.abspath(__file__)) + "/" + puma_config.NLP_FILE_PATH)
