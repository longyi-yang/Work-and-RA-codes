# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:25:30 2023

@author: 53383
"""

import pandas as pd
import os

directory = r'D:\Personal\Desktop\文献\数据\人口预测\Lifetable'
SSP16 = ['SSP16-2022','SSP16-2023','SSP16-2024','SSP16-2025','SSP16-2026','SSP16-2027','SSP16-2028',
         'SSP16-2029','SSP16-2030']
SSP26 = ['SSP26-2022','SSP26-2023','SSP26-2024','SSP26-2025','SSP26-2026','SSP26-2027','SSP26-2028',
         'SSP26-2029','SSP26-2030']
SSP36 = ['SSP36-2022','SSP36-2023','SSP36-2024','SSP36-2025','SSP36-2026','SSP36-2027','SSP36-2028',
         'SSP36-2029','SSP36-2030']
for i in SSP16:
    df = pd.read_excel(directory, sheet_name= i)
    
df= pd.read_excel(io='./lifetable.xlsx', sheet_name= 'SSP16-2022')
df['Mid-Year population high'] = df['Mid-Year population'] * 0.5
df['Mid-Year population medium'] = df['Mid-Year population'] * 0.35
df['Mid-Year population low'] = df['Mid-Year population'] * 0.15
df['Deaths high'] = df['Deaths'] *0.5
df['Deaths mdeium'] = df['Deaths'] *0.35
df['Deaths low'] = df['Deaths'] *0.15
df_high = df[['From','To','Mid-Year population high','Deaths high']]
df_high = df_high.round(decimals=0)
df_medium =
df_low = 
df_high.to_csv('./lifetables/SSP16-2022-high.csv',index= False,sep=';') 
