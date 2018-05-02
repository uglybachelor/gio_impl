# -*- coding: UTF-8 -*-
import sys
import pandas as pd
from metrics import *
from openpyxl import *

fullHeader = [u'标识符', u'类型', u'名称', u'描述']
configEventHeader = [u'名称', u'描述', u'标识符', u'事件级变量', u'触发时机描述', u'事件类型']
configVarHeader = [u'变量名称', u'变量描述', u'变量标识符', u'变量类型']
configPVarHeader = [u'变量名称', u'变量描述', u'变量标识符']
configEVarHeader = [u'变量名称', u'变量描述', u'变量标识符', u'归因方式', u'有效时间']
configUVarHeader = [u'变量名称', u'变量描述', u'变量标识符', u'归因方式']
codeEventHeader = [u'事件名称', u'事件标识符', u'事件级变量', u'触发时机描述', u'iOS代码', u'Android代码', u'JS代码']
codePVarHeader = [u'变量名称', u'变量标识符', u'变量触发时机', u'iOS代码', u'Android代码', u'JS代码']
codeEVarHeader = [u'变量名称', u'变量标识符', u'变量触发时机', u'iOS代码', u'Android代码', u'JS代码']
codeUVarHeader = [u'变量名称', u'变量标识符', u'变量触发时机', u'iOS代码', u'Android代码', u'JS代码']

outPutFileSheetNames = [u'所有事件及变量汇总', u'打点管理配置（事件）', u'打点管理配置（事件级变量）',
        u'打点管理配置（页面级变量）', u'打点管理配置（转化变量）', u'打点管理配置（用户变量）',u'实施代码（事件）',
        u'实施代码（页面级变量）', u'实施代码（转化变量）', u'实施代码（用户变量）']

# convert custom objects to dataframes
def convertToDF(objList):

    events = objList[0]
    eNum = len(events)
    vars = objList[1]
    vNum = len(vars)
    pVars = objList[2]
    pNum = len(pVars)
    eVars = objList[3]
    eVNum = len(eVars)
    uVars = objList[4]
    uNum = len(uVars)

    eventsIndicator = [e.getIndicator() for e in events]
    eventsName = [e.getName() for e in events]
    eventsDesc = [e.getDesc() for e in events]
    eventsType = [e.getType() for e in events]
    eventsTrigger = [e.getTrigger() for e in events]
    eventsVarList = [e.getVarList() for e in events]
    eventsCType = [e.getCType() for e in events]

    varIndicator = [v.getIndicator() for v in vars]
    varName = [v.getName() for v in vars]
    varDesc = [v.getDesc() for v in vars]
    varType = [v.getVType() for v in vars]

    pVarIndicator = [p.getIndicator() for p in pVars]
    pVarName = [p.getName() for p in pVars]
    pVarDesc = [p.getDesc() for p in pVars]
    pVarTrigger = [p.getTrigger() for p in pVars]

    eVarIndicator = [ev.getIndicator() for ev in eVars]
    eVarName = [ev.getName() for ev in eVars]
    eVarDesc = [ev.getDesc() for ev in eVars]
    eVarAttr = [ev.getAttribution() for ev in eVars]
    eVarEffT = [ev.getEffectiveTime() for ev in eVars]
    eVarTrigger = [ev.getTrigger() for ev in eVars]

    uVarIndicator = [u.getIndicator() for u in uVars]
    uVarName = [u.getName() for u in uVars]
    uVarDesc = [u.getDesc() for u in uVars]
    uVarAttr = [u.getAttribution() for u in uVars]
    uVarTrigger = [u.getTrigger() for u in uVars]

    # create dataframes for each sheet
    fullDF = pd.DataFrame(columns=fullHeader)
    fullDF[u'标识符'] = eventsIndicator + varIndicator + pVarIndicator + eVarIndicator + uVarIndicator
    fullDF[u'名称'] = eventsName + varName + pVarName + eVarName + uVarName
    fullDF[u'描述'] = eventsDesc + varDesc + pVarDesc + eVarDesc + uVarDesc

    configEventDF = pd.DataFrame(columns=configEventHeader)
    configEventDF[u'名称'] = eventsName
    configEventDF[u'描述'] = eventsDesc
    configEventDF[u'标识符'] = eventsIndicator
    configEventDF[u'事件级变量'] = eventsVarList
    configEventDF[u'触发时机描述'] = eventsTrigger
    configEventDF[u'事件类型'] = eventsCType

    configVarDF = pd.DataFrame(columns=configVarHeader)
    configVarDF[u'变量名称'] = varName
    configVarDF[u'变量描述'] = varDesc
    configVarDF[u'变量标识符'] = varIndicator
    configVarDF[u'变量类型'] = varType

    configPVarDF = pd.DataFrame(columns=configPVarHeader)
    configPVarDF[u'变量名称'] = pVarName
    configPVarDF[u'变量描述'] = pVarDesc
    configPVarDF[u'变量标识符'] = pVarIndicator

    configEVarDF = pd.DataFrame(columns=configEVarHeader)
    configEVarDF[u'变量名称'] = eVarName
    configEVarDF[u'变量描述'] = eVarDesc
    configEVarDF[u'变量标识符'] = eVarIndicator
    configEVarDF[u'归因方式'] = eVarAttr
    configEVarDF[u'有效时间'] = eVarEffT

    configUVarDF = pd.DataFrame(columns=configUVarHeader)
    configUVarDF[u'变量名称'] = uVarName
    configUVarDF[u'变量描述'] = uVarDesc
    configUVarDF[u'变量标识符'] = uVarIndicator
    configUVarDF[u'归因方式'] = uVarAttr

    codeEventDF = pd.DataFrame(columns=codeEventHeader)
    codeEventDF[u'事件名称'] = eventsName
    codeEventDF[u'事件标识符'] = eventsIndicator
    codeEventDF[u'事件级变量'] = eventsVarList
    codeEventDF[u'iOS代码'] = genEventCodes(eventsIndicator, eventsVarList, eventsType)[0]
    codeEventDF[u'Android代码'] = genEventCodes(eventsIndicator, eventsVarList, eventsType)[1]
    codeEventDF[u'JS代码'] = genEventCodes(eventsIndicator, eventsVarList, eventsType)[2]
    codeEventDF[u'触发时机描述'] = eventsTrigger

    codePVarDF = pd.DataFrame(columns=codePVarHeader)
    codePVarDF[u'变量名称'] = pVarName
    codePVarDF[u'变量标识符'] = pVarIndicator
    codePVarDF[u'变量触发时机'] = pVarTrigger
    codePVarDF[u'iOS代码'] = genVarCodes(pVarIndicator, 'pVar')[0]
    codePVarDF[u'Android代码'] = genVarCodes(pVarIndicator, 'pVar')[1]
    codePVarDF[u'JS代码'] = genVarCodes(pVarIndicator, 'pVar')[2]

    codeEVarDF = pd.DataFrame(columns=codeEVarHeader)
    codeEVarDF[u'变量名称'] = eVarName
    codeEVarDF[u'变量标识符'] = eVarIndicator
    codeEVarDF[u'变量触发时机'] = eVarTrigger
    codeEVarDF[u'iOS代码'] = genVarCodes(eVarIndicator, 'eVar')[0]
    codeEVarDF[u'Android代码'] = genVarCodes(eVarIndicator, 'eVar')[1]
    codeEVarDF[u'JS代码'] = genVarCodes(eVarIndicator, 'eVar')[2]

    codeUVarDF = pd.DataFrame(columns=codeUVarHeader)
    codeUVarDF[u'变量名称'] = uVarName
    codeUVarDF[u'变量标识符'] = uVarIndicator
    codeUVarDF[u'变量触发时机'] = uVarTrigger
    codeUVarDF[u'iOS代码'] = genVarCodes(uVarIndicator, 'uVar')[0]
    codeUVarDF[u'Android代码'] = genVarCodes(uVarIndicator, 'uVar')[1]
    codeUVarDF[u'JS代码'] = genVarCodes(uVarIndicator, 'uVar')[2]

    return [fullDF, configEventDF, configVarDF, configPVarDF, configEVarDF,
        configUVarDF, codeEventDF, codePVarDF, codeEVarDF, codeUVarDF]

# generate event codes
def genEventCodes(indicators, varLists, eTypes):
    iCodes = []
    aCodes = []
    jCodes = []
    for e in range(len(indicators)):
        iCode = ''
        aCode = ''
        jCode = ''
        if eTypes[e] == u'无参计单':
            iCode = '[Growing track: @"' + indicators[e] + '"];'
            aCode = 'GrowingIO.getInstance().track("' + indicators[e] + '");'
            jCode = 'gio("track", "' + indicators[e] + '");'
        elif eTypes[e] == u'有参计单':
            iVarCodes = ''
            for i in range(len(varLists[e])-1):
                iVarCodes = iVarCodes + '@"' + varLists[e][i] + u'": @"参数值", '
            iVarCodes = iVarCodes + '@"' + varLists[e][len(varLists[e])-1] + u'": @"参数值"'
            iCode = '[Growing track: @"' + indicators[e] + '" withVariable: @{' + iVarCodes + '}];'

            aVarCodes = ''
            for i in range(len(varLists[e])-1):
                aVarCodes = aVarCodes + '"' + varLists[e][i] + u'": "参数值", '
            aVarCodes = aVarCodes + '"' + varLists[e][len(varLists[e])-1] + u'": "参数值"'
            aCode = 'GrowingIO.getInstance().track("' + indicators[e] + '", {' +aVarCodes + '});'

            jVarCodes = ''
            for i in range(len(varLists[e])-1):
                jVarCodes = jVarCodes + '"' + varLists[e][i] + u'": "参数值", '
            jVarCodes = jVarCodes + '"' + varLists[e][len(varLists[e])-1] + u'": "参数值"'
            jCode = 'gio("track", "' + indicators[e] + '", {' + jVarCodes + '});'
        elif eTypes[e] == u'无参计复':
            iCode = '[Growing track: @"' + indicators[e] + '" withNumber:@10];'
            aCode = 'GrowingIO.getInstance().track("' + indicators[e] + '", 10);'
            jCode = 'gio("track", "' + indicators[e] + '", 10);'
        elif eTypes[e] == u'有参计复':
            iVarCodes = ''
            for i in range(len(varLists[e])-1):
                iVarCodes = iVarCodes + '@"' + varLists[e][i] + u'": @"参数值", '
            iVarCodes = iVarCodes + '@"' + varLists[e][len(varLists[e])-1] + u'": @"参数值"'
            iCode = '[Growing track: @"' + indicators[e] + '" withNumber:@10 andVariable: @{' + iVarCodes + '}];'

            aVarCodes = ''
            for i in range(len(varLists[e])-1):
                aVarCodes = aVarCodes + '"' + varLists[e][i] + u'": "参数值", '
            aVarCodes = aVarCodes + '"' + varLists[e][len(varLists[e])-1] + u'": "参数值"'
            aCode = 'GrowingIO.getInstance().track("' + indicators[e] + '", 10, {' +aVarCodes + '});'

            jVarCodes = ''
            for i in range(len(varLists[e])-1):
                jVarCodes = jVarCodes + '"' + varLists[e][i] + u'": "参数值", '
            jVarCodes = jVarCodes + '"' + varLists[e][len(varLists[e])-1] + u'": "参数值"'
            jCode = 'gio("track", "' + indicators[e] + '", 10, {' + jVarCodes + '});'
        iCodes.append(iCode)
        aCodes.append(aCode)
        jCodes.append(jCode)

    return [iCodes, aCodes, jCodes]

#generate variable codes
def genVarCodes(indicators, vType):
    iCodes = []
    aCodes = []
    jCodes = []

    for v in range(len(indicators)):
        iCode = ''
        aCode = ''
        jCode = ''
        if vType == 'pVar':
            iCode = '[GrowingIO setPageVariable: @{@"' + indicators[v] + u'": @"参数值"} toViewController: myViewController];'
            aCode = 'GrowingIO.getInstance().setPageVariable(myActivity'  + ', {"' + indicators[v] + u'": "参数值"});'
            jCode = 'gio("page.set", {"' + indicators[v] + u'": "参数值"});'
        elif vType == 'eVar':
            iCode = '[GrowingIO setEvar: @{@"' + indicators[v] + u'": @"参数值"}];'
            aCode = 'GrowingIO.getInstance().setEvar({"' + indicators[v] + u'": "参数值"});'
            jCode = 'gio("evar.set", {"' + indicators[v] + u'": "参数值"});'
        elif vType == 'uVar':
            iCode = '[GrowingIO setPeopleVariable: @{@"' + indicators[v] + u'": @"参数值"}];'
            aCode = 'GrowingIO.getInstance().setPeopleVariable({"' + indicators[v] + u'": "参数值"});'
            jCode = 'gio("people.set", {"' + indicators[v] + u'": "参数值"});'
        iCodes.append(iCode)
        aCodes.append(aCode)
        jCodes.append(jCode)

    return [iCodes, aCodes, jCodes]


# generate excel file
def genFile(out_sheets):
    writer = pd.ExcelWriter('GrowingIO实施文档.xlsx')
    for i in range(len(out_sheets)):
        out_sheets[i].to_excel(writer, outPutFileSheetNames[i])
    try:
        writer.save()
    except Exception, e:
        print e
        print u'输出文件生成失败!'
        sys.exit


    wb = load_workbook('GrowingIO实施文档.xlsx')

    print u'输出文件已生成~~~'

__all__ = ['convertToDF', 'genFile']
