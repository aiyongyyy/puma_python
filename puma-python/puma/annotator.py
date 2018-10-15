

import logging

from .utils import fileutils

import queue


class DictAnnotator:

    def __init__(self, annotationRuleDictPath, whiteEntityTypeOnly=False, entityTypeWhiteListFilePath=""):

        self.loadedAnnotationRuleDictPath = ""

        if not annotationRuleDictPath:
            logging.error("Loading dict occurs an error.")
            return
        elif self.loadedAnnotationRuleDictPath == annotationRuleDictPath:
            logging.info("Annotation rule dict is successfully loaded.")
            return
        else:

            whiteEntityTypeList = []
            if whiteEntityTypeOnly:
                whiteEntityTypeList = fileutils.loadList(entityTypeWhiteListFilePath)

            filePathQueue = queue.Queue()




