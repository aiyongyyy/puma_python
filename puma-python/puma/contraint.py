import datetime
from .model import *
from .utils.constantsdefine import *
from .extraction import *
import dateutil.relativedelta

class ConstrainBase:

    def ConstraintParse(self, map):
        pass

class DateConstrainRelativeNormal(ConstrainBase):

    def __init__(self):

        self.typeList = ["relativeposition_day", "relativeposition_week", "relativeposition_month", "relativeposition_quat", "relativeposition_year"]

    def ConstraintParse(self, map):
        dateMap = map["date"]
        constraint = None

        for type in self.typeList:
            if type in dateMap:
                constraint = self.extractDateTimeType(dateMap[type])
        return constraint

    def extractDateTimeType(self, relativeposition):

        constraintDate = {}

        startDate = None
        endDate = None

        if relativeposition == "今天" or relativeposition == "今日":
            startDate = EntityDateModel(datetime.datetime.now())
            endDate = EntityDateModel(startDate.dateTime + datetime.timedelta(days=1))
        elif relativeposition == "明天":
            startDate = EntityDateModel(datetime.datetime.now()+ datetime.timedelta(days=1))
            endDate = EntityDateModel(startDate.dateTime + datetime.timedelta(days=1))
        elif relativeposition == "后天" or relativeposition == "后一天":
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=2))
            endDate = EntityDateModel(startDate.dateTime + datetime.timedelta(days=1))
        elif relativeposition == "大后天":
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=3))
            endDate = EntityDateModel(startDate.dateTime + datetime.timedelta(days=1))
        elif relativeposition == "昨天" or relativeposition == "前一天" or relativeposition == "昨日":
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-1))
            endDate = EntityDateModel(startDate.dateTime + datetime.timedelta(days=1))
        elif relativeposition == "前天":
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-2))
            endDate = EntityDateModel(startDate.dateTime + datetime.timedelta(days=1))
        elif relativeposition == "大前天":
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-3))
            endDate = EntityDateModel(startDate.dateTime + datetime.timedelta(days=1))
        elif relativeposition == "本周" or relativeposition == "这周" or relativeposition == "这一周":
            period = datetime.datetime.now().weekday() - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period))
            endDate = EntityDateModel(startDate.dateTime + datetime.timedelta(weeks=1))
        elif relativeposition == "上周" or relativeposition == "上一周":
            period = datetime.datetime.now().weekday() - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + datetime.timedelta(weeks=-1))
            endDate = EntityDateModel(startDate.dateTime + datetime.timedelta(weeks=1))
        elif relativeposition == "上上周":
            period = datetime.datetime.now().weekday() - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + datetime.timedelta(weeks=-2))
            endDate = EntityDateModel(startDate.dateTime + datetime.timedelta(weeks=1))
        elif relativeposition == "下周" or relativeposition == "下一周":
            period = datetime.datetime.now().weekday() - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + datetime.timedelta(weeks=1))
            endDate = EntityDateModel(startDate.dateTime + datetime.timedelta(weeks=1))
        elif relativeposition == "下下周":
            period = datetime.datetime.now().weekday() - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + datetime.timedelta(weeks=2))
            endDate = EntityDateModel(startDate.dateTime + datetime.timedelta(weeks=2))
        elif relativeposition == "本月" or relativeposition == "这月" or relativeposition == "这一月" or relativeposition == "这个月":
            period = datetime.datetime.now().day - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(months=1))
        elif relativeposition == "上月" or relativeposition == "上个月" or relativeposition == "上一月":
            period = datetime.datetime.now().day - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(months=-1))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(months=1))
        elif relativeposition == "上上月" or relativeposition == "上上个月":
            period = datetime.datetime.now().day - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(months=-2))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(months=1))
        elif relativeposition == "下月" or relativeposition == "下个月" or relativeposition == "下一月":
            period = datetime.datetime.now().day - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(months=1))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(months=1))
        elif relativeposition == "下下月" or relativeposition == "下下个月":
            period = datetime.datetime.now().day - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(months=2))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(months=1))
        elif relativeposition == "本季度" or relativeposition == "这季度" or relativeposition == "这个季度":
            period = datetime.datetime.now().day - 1
            period_month = (datetime.datetime.now().month  + 2)% 3
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(months=-period_month))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(months=3))
        elif relativeposition == "上季度" or relativeposition == "上个季度" or relativeposition == "上一季度":
            period = datetime.datetime.now().day - 1
            period_month = (datetime.datetime.now().month + 2) % 3 + 3
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(months=-period_month))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(months=3))
        elif relativeposition == "上上季度" or relativeposition == "上上个季度":
            period = datetime.datetime.now().day - 1
            period_month = (datetime.datetime.now().month + 2) % 3 + 6
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(months=-period_month))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(months=3))
        elif relativeposition == "下季度" or relativeposition == "下个季度":
            period = datetime.datetime.now().day - 1
            period_month = (datetime.datetime.now().month + 2) % 3 - 3
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(months=-period_month))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(months=3))
        elif relativeposition == "下下季度" or relativeposition == "下下个季度":
            period = datetime.datetime.now().day - 1
            period_month = (datetime.datetime.now().month + 2) % 3 - 6
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(months=-period_month))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(months=3))
        elif relativeposition == "今年":
            period = datetime.datetime.now().timetuple().tm_yday - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(years=1))
        elif relativeposition == "明年":
            period = datetime.datetime.now().timetuple().tm_yday - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(years=1))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(years=1))
        elif relativeposition == "后年":
            period = datetime.datetime.now().timetuple().tm_yday - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(years=2))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(years=1))
        elif relativeposition == "大后年":
            period = datetime.datetime.now().timetuple().tm_yday - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(years=3))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(years=1))
        elif relativeposition == "去年":
            period = datetime.datetime.now().timetuple().tm_yday - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(years=-1))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(years=1))
        elif relativeposition == "前年":
            period = datetime.datetime.now().timetuple().tm_yday - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(years=-2))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(years=1))
        elif relativeposition == "大前年":
            period = datetime.datetime.now().timetuple().tm_yday - 1
            startDate = EntityDateModel(datetime.datetime.now() + datetime.timedelta(days=-period) + dateutil.relativedelta.relativedelta(years=-3))
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(years=1))

        if startDate is None and endDate is None:
            return None
        else:
            endDate = EntityDateModel(endDate.dateTime + datetime.timedelta(days=-1))
            constraintDate[CONSTRAIN_STARTDATE] = startDate
            constraintDate[CONSTRAIN_ENDDATE] = endDate
            return constraintDate

class DateConstrainCalendarPeriod(ConstrainBase):

    def __init__(self):
        pass

    def ConstraintParse(self, map):
        dateMap = map["date"]
        constraint = self.extractDateCalendar(dateMap["calendar_start"], dateMap["calendar_end"])
        return constraint

    def extractDateCalendar(self, calendar_start, calendar_end):
        constraintDate = {}

        startDate = None
        endDate = None

        if not calendar_start is None:
            startDate = EntityDateModel(calendar_start)
        if not calendar_end is None:
            endDate = EntityDateModel(calendar_end)

        if startDate is None and endDate is None:
            return None
        else:
            constraintDate[CONSTRAIN_STARTDATE] = startDate
            constraintDate[CONSTRAIN_ENDDATE] = endDate
            return constraintDate


class DateConstrainCalendarRange(ConstrainBase):

    def __init__(self):
        pass

    def ConstraintParse(self, map):
        dateMap = map["date"]
        constraint = self.extractDateCalendar(dateMap["calendar_year"], dateMap["calendar_quat"],
				dateMap["calendar_month"], dateMap["calendar_day"], dateMap["relativeposition"])
        return constraint


    def extractDateCalendar(self, calendar_year, calendar_quat, calendar_month, calendar_day, relativeposition):
        constraintDate = {}

        startDate = None
        endDate = None
        pointDate = None

        if not calendar_year is None:
            pointDate = EntityDateModel(calendar_year)
        elif not calendar_quat is None:
            pointDate = EntityDateModel(calendar_quat)
        elif not calendar_month is None:
            pointDate = EntityDateModel(calendar_month)
        elif not calendar_day is None:
            pointDate = EntityDateModel(calendar_day)

        if relativeposition == "before":
            startDate = None
            endDate = pointDate
        elif relativeposition == "after":
            startDate = pointDate
            endDate = None
        elif relativeposition == "forward":
            startDate = pointDate
            endDate = EntityDateModel(datetime.datetime.now())
        elif relativeposition == "backward":
            startDate = EntityDateModel(datetime.datetime.now())
            endDate = pointDate

        if startDate is None and endDate is None:
            return None
        else:
            constraintDate[CONSTRAIN_STARTDATE] = startDate
            constraintDate[CONSTRAIN_ENDDATE] = endDate
            return constraintDate


class DateConstrainCalendarNormal(ConstrainBase):

    def __init__(self):
        pass

    def ConstraintParse(self, map):
        dateMap = map["date"]


        constraint = self.extractDateCalendar(None if not "calenar_year" in dateMap else dateMap["calendar_year"], None if not "calendar_halfyear" in dateMap else dateMap["calendar_halfyear"],
				None if not "calendar_quat" in dateMap else dateMap["calendar_quat"], None if not "calendar_month" in dateMap else dateMap["calendar_month"], None if not "calendar_day" in dateMap else dateMap["calendar_day"])

        return constraint


    def extractDateCalendar(self, calendar_year, calendar_halfyear, calendar_quat, calendar_month, calendar_day):
        constraintDate = {}

        startDate = None
        endDate = None

        if not calendar_year is None:
            startDate = EntityDateModel(calendar_year)
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(years=1))
        elif not calendar_halfyear is None:
            startDate = EntityDateModel(calendar_halfyear)
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(months=6))
        elif not calendar_quat is None:
            startDate = EntityDateModel(calendar_quat)
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(months=3))
        elif not calendar_month is None:
            startDate = EntityDateModel(calendar_month)
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(months=1))
        elif not calendar_day is None:
            startDate = EntityDateModel(calendar_day)
            endDate = EntityDateModel(startDate.dateTime + dateutil.relativedelta.relativedelta(days=1))

        if startDate is None and endDate is None:
            return None
        else:
            endDate = EntityDateModel(endDate.dateTime + datetime.timedelta(days=-1))
            constraintDate[CONSTRAIN_STARTDATE] = startDate
            constraintDate[CONSTRAIN_ENDDATE] = endDate
            return constraintDate


class DateConstrainRelativeRange(ConstrainBase):

    def __init__(self):
        pass

    def ConstraintParse(self, map):
        dateMap = map["date"]
        constraint = self.extractDateTimeType(dateMap["frequency"], dateMap["relativeposition"], float(dateMap["number"]))
        return constraint


    def extractDateTimeType(self, frequency, relativeposition, number):

        constraintDate = {}

        startDate = None
        endDate = None

        if frequency == "年":
            if relativeposition == "before":
                startDate = None
                if number < 1:
                    endDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(months=int(number * 12)))
                else:
                    endDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(years=int(number)))
            elif relativeposition == "after":
                if number < 1:
                    startDate = EntityDateModel(datetime.datetime.now() + dateutil.relativedelta.relativedelta(months=int(number * 12)))
                else:
                    startDate = EntityDateModel(datetime.datetime.now() + dateutil.relativedelta.relativedelta(years=int(number)))
                endDate = None
            elif relativeposition == "forward":
                if number < 1:
                    startDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(months=int(number*12)))
                else:
                    startDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(years=int(number)))
                endDate = EntityDateModel(datetime.datetime.now())
            elif relativeposition == "backward":
                startDate = EntityDateModel(datetime.datetime.now())
                if number < 1:
                    endDate = EntityDateModel(datetime.datetime.now() + dateutil.relativedelta.relativedelta(months=int(number * 12)))
                else:
                    endDate = EntityDateModel(datetime.datetime.now() + dateutil.relativedelta.relativedelta(years=int(number)))

        elif frequency == "月":
            if relativeposition == "before":
                startDate = None
                if number < 1:
                    endDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(days=int(number * 30)))
                else:
                    endDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(months=int(number)))
            elif relativeposition == "after":
                if number < 1:
                    startDate = EntityDateModel(datetime.datetime.now() + dateutil.relativedelta.relativedelta(days=int(number * 30)))
                else:
                    startDate = EntityDateModel(datetime.datetime.now() + dateutil.relativedelta.relativedelta(months=int(number)))
                endDate = None
            elif relativeposition == "forward":
                if number < 1:
                    startDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(days=int(number * 30)))
                else:
                    startDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(months=int(number)))
                endDate = EntityDateModel(datetime.datetime.now())
            elif relativeposition == "backward":
                startDate = EntityDateModel(datetime.datetime.now())
                if number < 1:
                    endDate = EntityDateModel(datetime.datetime.now() + dateutil.relativedelta.relativedelta(days=int(number * 30)))
                else:
                    endDate = EntityDateModel(datetime.datetime.now() + dateutil.relativedelta.relativedelta(months=int(number)))

        elif frequency == "周":
            if relativeposition == "before":
                startDate = None
                endDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(weeks=int(number)))
            elif relativeposition == "after":
                startDate = EntityDateModel(datetime.datetime.now() + dateutil.relativedelta.relativedelta(weeks=int(number)))
                endDate = None
            elif relativeposition == "forward":
                startDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(weeks=int(number)))
                endDate = EntityDateModel(datetime.datetime.now())
            elif relativeposition == "backward":
                startDate = EntityDateModel(datetime.datetime.now())
                endDate = EntityDateModel(datetime.datetime.now() + dateutil.relativedelta.relativedelta(weeks=int(number)))
        elif frequency == "日":
            if relativeposition == "before":
                startDate = None
                endDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(days=int(number)))
            elif relativeposition == "after":
                startDate = EntityDateModel(datetime.datetime.now() + dateutil.relativedelta.relativedelta(days=int(number)))
                endDate = None
            elif relativeposition == "forward":
                startDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(days=int(number)))
                endDate = EntityDateModel(datetime.datetime.now())
            elif relativeposition == "backward":
                startDate = EntityDateModel(datetime.datetime.now())
                endDate = EntityDateModel(datetime.datetime.now() + dateutil.relativedelta.relativedelta(days=int(number)))
        elif frequency == "季度":
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            if relativeposition == "before":
                startDate = None
                endDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(months=month%3 -1 + int(number*3)) - datetime.timedelta(days=day))
            elif relativeposition == "after":
                startDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(months=month%3 -1 - int(number*3)) - datetime.timedelta(days=day))
                endDate = None
            elif relativeposition == "forward":
                startDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(months=month%3 -1 + int(number*3)) - datetime.timedelta(days=day))
                endDate = EntityDateModel(datetime.datetime.now())
            elif relativeposition == "backward":
                startDate = EntityDateModel(datetime.datetime.now())
                endDate = EntityDateModel(datetime.datetime.now() - dateutil.relativedelta.relativedelta(months=month%3 -1 - int(number*3)) - datetime.timedelta(days=day))


        if startDate is None and endDate is None:
            return  None
        else:
            constraintDate[CONSTRAIN_STARTDATE] = startDate
            constraintDate[CONSTRAIN_ENDDATE] = endDate
            return constraintDate





class DateConstrain:

    def __init__(self):
        self.dateConstrainRelativeNormal = DateConstrainRelativeNormal()
        self.dateConstrainRelativeRange = DateConstrainRelativeRange()
        self.dateConstrainCalendarNormal = DateConstrainCalendarNormal()
        self.dateConstrainCalendarPeriod = DateConstrainCalendarPeriod()
        self.dateConstrainCalendarRange = DateConstrainCalendarRange()

    def getDateConstraint(self, patternDate):
        if not patternDate is None:
            date = self.getEntitytypeDateConstrain(patternDate)
            if not date is None:
                return date

        return self.getDefaultDateConstrain(patternDate.scene, patternDate.entityType)

    def getEntitytypeDateConstrain(self, patternDate):
        constrain = None
        if patternDate.entityType == "date_relative_normal_extraction":
            constrain = self.dateConstrainRelativeNormal
        elif patternDate.entityType == "date_relative_range_extraction" or patternDate.entityType == "date_relative_range_custorm_extraction":
            constrain = self.dateConstrainRelativeRange
        elif patternDate.entityType == "date_calendar_normal_extraction":
            constrain = self.dateConstrainCalendarNormal
        elif patternDate.entityType == "date_calendar_period_extraction":
            constrain = self.dateConstrainCalendarPeriod
        elif patternDate.entityType == "date_calendar_range_extraction":
            constrain = self.dateConstrainCalendarRange

        if not constrain is None:
            try:
                parseMapModel = puma_parsePattern.ParseQueryByPattern(patternDate)
                parsingMap = parseMapModel.state_parsing_map
                constraintDate = constrain.ConstraintParse(parsingMap)
                if not constraintDate is None:
                    return self.buildDateValue(constraintDate)

            except Exception as e:
                print(e)

        return None


    def getDefaultDateConstrain(self, scene, entityType):
        constraintDate = {}
        if scene.getSceneClassification() == 0:
            return None
        elif scene.getSceneClassification() == 1:
            return None
        else:
            startDate = EntityDateModel(datetime.datetime.now())
            endDdate = EntityDateModel(startDate.dateTime + datetime.timedelta(days=1))
            constraintDate[CONSTRAIN_STARTDATE] = startDate
            constraintDate[CONSTRAIN_ENDDATE] = endDdate

        return self.buildDateValue(constraintDate)


    def buildDateValue(self, constraintDate):
        date = ""
        date += "["
        if not constraintDate[CONSTRAIN_STARTDATE] is None:
            date += constraintDate[CONSTRAIN_STARTDATE].dateTime.strftime(FORMAT_DATE_EN)
        else:
            date += " "
        date += ","
        if not constraintDate[CONSTRAIN_ENDDATE] is None:
            date += constraintDate[CONSTRAIN_ENDDATE].dateTime.strftime(FORMAT_DATE_EN)
        else:
            date += " "
        date+= ")"

        return date


puma_dateConstrain = DateConstrain()