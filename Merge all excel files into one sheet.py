# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 18:23:11 2022

@author: 53383
"""
#50MW
230-12

#50MW
import pandas as pd
import os
#直接把多个excel的sheets放到一个sheet里
directory = r'D:\Personal\Desktop\merge\50MW'
filenames = os.listdir(directory)
index = 0
dfs = []
for name in filenames:
    print(index)
    i = pd.read_excel(os.path.join(directory,name),
                      sheet_name = 1)
    top_row = pd.DataFrame({'海上成本拆分':[name]})
    i = pd.concat([top_row,i]).reset_index(drop = True)
    dfs.append(i)
    index += 1
df = pd.concat(dfs)
df.to_excel( r'D:\Personal\Desktop\merge\50MW\50MW_merged.xlsx', index = False)

#从merge excel生成all in one sheet
df_dict = {}
sheet_list = []
excel = pd.ExcelFile('.\50MW\50MW-merge.xlsx')
sheets = excel.sheet_names[1:]
for s in sheets:
    i = pd.read_excel('.\50MW\50MW-merge.xlsx',sheet_name = s)
    i.iloc[0,0] = s
    sheet_list.append(i)
sheet_all = pd.concat(sheet_list)
sheet_all.to_excel('.\\50MW-merged_version.xlsx', index = False)

#125MW
import pandas as pd
import os
#直接把多个excel的sheets放到一个sheet里
directory = r'D:\Personal\Desktop\merge\125MW'
filenames = os.listdir(directory)
index = 0
dfs = []
for name in filenames:
    print(index)
    i = pd.read_excel(os.path.join(directory,name),
                      sheet_name = 1)
    top_row = pd.DataFrame({'海上成本拆分':[name]})
    i = pd.concat([top_row,i]).reset_index(drop = True)
    dfs.append(i)
    index += 1
df = pd.concat(dfs)
df.to_excel( r'D:\Personal\Desktop\merge\125MW\125MW_merged.xlsx', index = False)

#从merge excel生成all in one sheet
import pandas as pd
all_dfs = pd.read_excel('.\125MW\125MW-merge.xlsx', sheet_name=None)
df = pd.concat(all_dfs, ignore_index=True)

import pandas as pd
df_dict = {}
sheet_list = []
excel = pd.ExcelFile('.\\海域与项目容量-merge.xlsx')
sheets = excel.sheet_names[1:]
for s in sheets:
    i = pd.read_excel('.\\海域与项目容量-merge.xlsx',sheet_name = s)
    i.iloc[0,0] = s
    sheet_list.append(i)
sheet_all = pd.concat(sheet_list)
sheet_all.to_excel('.\\海域与项目容量-merged_version.xlsx', index = False)




