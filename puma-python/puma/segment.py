
import logging
from . import model
from .utils.fileutils import *


class Segment:

    def __init__(self, segmentMethod="ansj"):
        self.segWords = []
        self.segmentMethod = segmentMethod

    def initialize(self, segmentWords):
        self.segWords = segmentWords

    def segmentQuery(self, queryModel):
        try:
            querySentence = queryModel.querySentence
            if queryModel.IS_SEARCH:
                querySentence  = querySentence[1 : len(querySentence) - 1]

            logging.info(querySentence + ":" + "".join(self.segWords))

            startPos = 0
            if queryModel.IS_SEARCH:
                startPos = 1
            for wordStr in self.segWords:
                queryModel.addWordModel(model.WordModel(wordStr, startPos, startPos+len(wordStr), "segment"), startPos)
                startPos += len(wordStr)

            return True


        except Exception as e:
            print(e)
            return False


puma_segment = Segment()


# class BaseSegment:
#
#     def __init__(self):
#         self.OPTION_DEFAULT = 1
#
#     def addUserLibraryPath(self, userLibraryPathList):
#         for libraryPath in userLibraryPathList:
#             lines = loadListFile(libraryPath)
#             for line in lines:
#                 words = line.strip().split("\\s+")
#                 self.addDynamicWord(words)
#
#     def addDynamicWord(self, words):
#         pass
#
#
#
#
#
#
#
# class WordSegment:
#
#     def __init__(self):
#         self.segment = BaseSegment()
#         self.
#
#     @classmethod
#     def



