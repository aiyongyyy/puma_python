import datetime
import logging
import re


a = "	1	2	3	4	"

b = a.split("\t")

str = "\."


patternyyyyMMddBlank = "([12][0-9]{3}|[0-9]{2})(/|\\\\.|-)(([1][0-2])|([0]?[1-9]))(/|\.|-)(([3][01])|([0-2]?[0-9]))"

resut = re.match(patternyyyyMMddBlank, "2018.01.01")


logging.basicConfig(level=logging.NOTSET)

logging.info(123)

a = [None]*3

import puma

query = "07.03,到,07.28,新闻"
query = "一周,内,新闻"
query = "三个月,之前,到,一个月,之前,新闻"
query = "2016,年,到,2017,年,的新闻"
query = "2016年5月1号,2016年5月3号,2016年10月,和,2017年5月5号到2017年5月10号,的新闻"
#query = "营业额,增长,百分之五十,的,公司"


puma.puma_query(query)



a = datetime.datetime(1,1,1)

b = a.strftime("%Y-%m-%d")


a = "1234567"


if not a is None:
    b = 1


class testclass:

    @classmethod
    def test2(cls):
        a.b = 1
        pass

    @staticmethod
    def test():
        a.b = 2
        pass

    def __init__(self):
        self.b = None
        self.a = 1

a = testclass()

b = testclass.__class__

d = testclass

e = b()

f = d()

c = []




for d in c:
    d.test()

a.test2()
if a.b is None:
    a.b = 1


a.b = a.a
a.c = a.b
if a:
    a = 1

a = [[1,2,3] for x in range(3)]

a[0].append(1)


import puma

print(1)