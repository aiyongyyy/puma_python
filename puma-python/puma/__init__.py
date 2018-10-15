from .service import *


def puma_query(query):

    result = AnalysisService.getDateRangeFeatureForQuestion(query)

    print(result)

    return result






if __name__ == "__main__":
    query = "07.03到07.28新闻"


    puma_query(query)











