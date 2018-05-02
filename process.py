# -*- coding: UTF-8 -*-
import pandas as pd
from metrics import *

# process event sheet
def eventProcessor(df):
    headers = df.columns.values
    events = []

    # drop NA
    df.dropna(axis=0, how='all', thresh=6, inplace=True)

    event_num = df.shape[0]
    vars_df = df.drop([h for h in headers if h.find(u'变量')==-1 ], axis=1)

    vars_nums = vars_df.count(axis=1)
    # get all vars and store in a list
    for i in range(event_num):
        vars_tmp = []
        e = Event(df.iloc[i][headers[0]], df.iloc[i][headers[1]], df.iloc[i][headers[2]],
            df.iloc[i][headers[3]], df.iloc[i][headers[4]], df.iloc[i][headers[5]], [])
        for j in range(vars_nums.iloc[i]):
            vars_tmp.append(vars_df.iloc[i][j])

        e.setVarList(vars_tmp)
        events.append(e)

    return events

# process var sheet
def varProcessor(df):
    headers = df.columns.values
    vars = []
    # drop NA
    df.dropna(axis=0, how='any', inplace=True)

    var_num = df.shape[0]
    for i in range(var_num):
        v = Var(df.iloc[i][headers[0]], df.iloc[i][headers[1]], df.iloc[i][headers[2]],
            df.iloc[i][headers[3]])
        vars.append(v)

    return vars

# process pVar sheet
def pVarProcessor(df):
    headers = df.columns.values
    pVars = []
    # drop NA
    df.dropna(axis=0, how='any', inplace=True)

    var_num = df.shape[0]
    for i in range(var_num):
        v = PVar(df.iloc[i][headers[0]], df.iloc[i][headers[1]], df.iloc[i][headers[2]],
            df.iloc[i][headers[3]])
        pVars.append(v)

    return pVars

# process eVar sheet
def eVarProcessor(df):
    headers = df.columns.values
    eVars = []
    # drop NA
    df.dropna(axis=0, how='any', inplace=True)

    var_num = df.shape[0]
    for i in range(var_num):
        v = EVar(df.iloc[i][headers[0]], df.iloc[i][headers[1]], df.iloc[i][headers[2]],
            df.iloc[i][headers[3]], df.iloc[i][headers[4]], df.iloc[i][headers[5]])
        eVars.append(v)

    return eVars

# process uVar sheet
def uVarProcessor(df):
    headers = df.columns.values
    uVars = []
    # drop NA
    df.dropna(axis=0, how='any', inplace=True)

    var_num = df.shape[0]
    for i in range(var_num):
        v = UVar(df.iloc[i][headers[0]], df.iloc[i][headers[1]], df.iloc[i][headers[2]], df.iloc[i][headers[3]], df.iloc[i][headers[4]])
        uVars.append(v)

    return uVars

__all__ = ['eventProcessor', 'varProcessor', 'pVarProcessor', 'eVarProcessor', 'uVarProcessor']
