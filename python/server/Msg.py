#!/usr/bin/env python
#-*- coding:utf-8 -*- 
from include import *

# @singleton
class Msg:
    """Socket send server msg struct""" 
    msgType = 0
    toSysKey = ""
    toKey = ""
    fromSysKey = ""
    fromKey = ""
    info = ""
    ok = ""
    data = {}

    def __init__(self):
        self.names = ("msgType", "toSysKey", "toKey", "fromSysKey", "fromKey", "id", "info", "ok", "data")
        self.snames = ("mt", "tsk", "tk", "fsk", "fk", "id", "in", "ok", "data")
        
        self.id = (str(uuid.uuid1())).split("-")[0]
        # self.info = "from terminal"
        self.msgType = -2                #默认广播本系统
        self.toSysKey = "raspberrypi"    #默认发给本系统 
        # msg.toKey = "1000"
    def init(self, jsonstr):
        fromMsg = yaml.safe_load(jsonstr)
        # print(fromMsg)
        names = self.names
        snames = self.snames
        for i in range(len(names)):
            setattr(self, names[i], fromMsg.get(snames[i], ""))
        if(self.data is None or self.data == ""):
            self.data = {}
        return
    def toString(self):
        res = {}
        names = self.names
        snames = self.snames
        for i in range(len(names)):
            if(hasattr(self, names[i])):
                attr = getattr(self, names[i])
                if(attr is not None and attr != ""):
                    res[snames[i]] = attr

        return json.dumps(res)

    def makeMsg(self, *args):
        i = 0
        for var in args:
            self.data["value" + str(i)] = var
            i += 1
        return