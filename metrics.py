# -*- coding: UTF-8 -*-

class Event:

    def __init__(self, indicator, name, desc, eType, cType, trigger, varList):
        self.__indicator = indicator
        self.__name = name
        self.__desc = desc
        self.__type = eType
        self.__trigger = trigger
        self.__varList = varList
        self.__cType = cType

    def setIndicator(self, str):
        if not str:
            raise ValueError('标识符不能为空！')
        else:
            self.__indicator = str

    def getIndicator(self):
        return self.__indicator

    def setName(self, str):
        if not str:
            raise ValueError('事件名称不能为空！')
        else:
            self.__name = str

    def getName(self):
        return self.__name

    def setDesc(self, str):
        if not str:
            raise ValueError('事件描述不能为空！')
        else:
            self.__desc = str

    def getDesc(self):
        return self.__desc

    def setType(self, str):
        if not str:
            raise ValueError('事件类型不能为空！')
        else:
            self.__type = str

    def getType(self):
        return self.__type

    def setTrigger(self, str):
        if not str:
            raise ValueError('触发时机不能为空！')
        else:
            self.__trigger = str

    def getTrigger(self):
        return self.__trigger

    def setVarList(self, lst):
        if not isinstance(lst, list):
            raise ValueError('事件指标的事件级变量必须是数组！')
        else:
            for i in range(len(lst)):
                self.__varList.append(lst[i].encode("ascii"))

    def getVarList(self):
        return self.__varList

    def setCType(self, str):
        if not str:
            raise ValueError('触发时机不能为空！')
        else:
            self.__cType = str

    def getCType(self):
        return self.__cType

class Var:

    def __init__(self, indicator, name, desc, vType):
        self.__indicator = indicator
        self.__name = name
        self.__desc = desc
        self.__vType = vType

    def setIndicator(self, str):
        if not str:
            raise ValueError('标识符不能为空！')
        else:
            self.__indicator = str

    def getIndicator(self):
        return self.__indicator

    def setName(self, str):
        if not str:
            raise ValueError('变量名称不能为空！')
        else:
            self.__name = str

    def getName(self):
        return self.__name

    def setDesc(self, str):
        if not str:
            raise ValueError('变量描述不能为空！')
        else:
            self.__desc = str

    def getDesc(self):
        return self.__desc

    def setVType(self, str):
        if not str:
            raise ValueError('变量描述不能为空！')
        else:
            self.__vType = str

    def getVType(self):
        return self.__vType

class PVar:

    def __init__(self, indicator, name, desc, trigger):
        self.__indicator = indicator
        self.__name = name
        self.__desc = desc
        self.__trigger = trigger

    def setIndicator(self, str):
        if not str:
            raise ValueError('标识符不能为空！')
        else:
            self.__indicator = str

    def getIndicator(self):
        return self.__indicator

    def setName(self, str):
        if not str:
            raise ValueError('变量名称不能为空！')
        else:
            self.__name = str

    def getName(self):
        return self.__name

    def setDesc(self, str):
        if not str:
            raise ValueError('变量描述不能为空！')
        else:
            self.__desc = str

    def getDesc(self):
        return self.__desc

    def setTrigger(self, str):
        if not str:
            raise ValueError('触发时机不能为空！')
        else:
            self.__trigger = str

    def getTrigger(self):
        return self.__trigger

class EVar:

    def __init__(self, indicator, name, desc, attr, eff_t, trigger):
        self.__indicator = indicator
        self.__name = name
        self.__desc = desc
        self.__attr = attr
        self.__eff_t = eff_t
        self.__trigger = trigger

    def setIndicator(self, str):
        if not str:
            raise ValueError('标识符不能为空！')
        else:
            self.__indicator = str

    def getIndicator(self):
        return self.__indicator

    def setName(self, str):
        if not str:
            raise ValueError('变量名称不能为空！')
        else:
            self.__name = str

    def getName(self):
        return self.__name

    def setDesc(self, str):
        if not str:
            raise ValueError('变量描述不能为空！')
        else:
            self.__desc = str

    def getDesc(self):
        return self.__desc

    def setAttribution(self, str):
        if not str:
            raise ValueError('归因方式不能为空！')
        else:
            self.__attr = str

    def getAttribution(self):
        return self.__attr

    def setEffectiveTime(self, str):
        if not str:
            raise ValueError('有效时间不能为空！')
        else:
            self.__eff_t = str

    def getEffectiveTime(self):
        return self.__eff_t

    def setTrigger(self, str):
        if not str:
            raise ValueError('触发时机不能为空！')
        else:
            self.__trigger = str

    def getTrigger(self):
        return self.__trigger

class UVar:

    def __init__(self, indicator, name, desc, attr, trigger):
        self.__indicator = indicator
        self.__name = name
        self.__desc = desc
        self.__attr = attr
        self.__trigger = trigger

    def setIndicator(self, str):
        if not str:
            raise ValueError('标识符不能为空！')
        else:
            self.__indicator = str

    def getIndicator(self):
        return self.__indicator

    def setName(self, str):
        if not str:
            raise ValueError('变量名称不能为空！')
        else:
            self.__name = str

    def getName(self):
        return self.__name

    def setDesc(self, str):
        if not str:
            raise ValueError('变量描述不能为空！')
        else:
            self.__desc = str

    def getDesc(self):
        return self.__desc

    def setAttribution(self, str):
        if not str:
            raise ValueError('归因方式不能为空！')
        else:
            self.__attr = str

    def getAttribution(self):
        return self.__attr

    def setTrigger(self, str):
        if not str:
            raise ValueError('触发时机不能为空！')
        else:
            self.__trigger = str

    def getTrigger(self):
        return self.__trigger
