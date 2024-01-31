# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#一个更换省份名称，然后把两个表合并，算总量的例子
import pandas as pd
#导入原表格
df1 = pd.read_excel(io = '.\\excel_1.xlsx')
df2 = pd.read_excel(io = '.\\excel_2.xlsx')
#把序号列删除掉
df1 = df1.iloc[:,1:]
df2 = df2.iloc[:,1:]
#替换第二张表格的省份名称
df2 = df2.replace(to_replace = ['新疆省','陕西省'],
                  value = ['新疆','陕西'])
#两张表的数据加总
df_m = df1.merge(df2, how='left', on= '省份') 
df_m['总量'] = df_m['数值_x'] + df_m['数值_y']
#把原有的不需要的列去除掉
不需要的列 = ['数值_x','数值_y']
for i in 不需要的列:
    df_m = df_m.drop([i],axis = 1)
#导出新excel表格
df_m.to_excel('合并后表格.xlsx')

import pandas as pd
#导入原表格
df = pd.concat(pd.read_excel(io = '.\\test.xlsx', sheet_name=None),
               ignore_index=True)

#两张表的数据加总
df_m = df1.merge(df2, how='down', on= '省份') 


#导出新excel表格
df_m.to_excel('合并后表格.xlsx')

#作产品谱图
import os
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
from adjustText import adjust_text
import math
import numpy as np
from matplotlib.pyplot import MultipleLocator
mpl.rcParams['font.sans-serif'] = ['SimHei']

# %% 陆上机型谱
#set working directory
os.chdir('D:\\Personal\\Desktop\\国内国际市场洞察\\国内\\产品谱')
#导入数据
data = pd.read_excel(r'.\\产品谱用.xlsx', sheet_name='陆上')
data = data[data['厂商'] != '华锐']
data = data[data['叶轮直径'] >= 170]
data = data[data['叶轮直径'] <= 220]
#作图
fig1 = plt.figure(1,figsize=(24,18),dpi=300)
#散点图
colors = ['b','red','darkorange','green','magenta','c']
markers = ['s','d','v','^','*','.']
厂商 = ['金风','远景','运达','明阳','上海电气','三一']
text_list = []
for index in range(6):
    单机容量 = data.loc[data['厂商'] == 厂商[index]]['单机容量']
    叶轮直径 = data.loc[data['厂商'] == 厂商[index]]['叶轮直径']
    plt.scatter(单机容量, 叶轮直径, 
                c=colors[index], cmap='brg', s=160, alpha=0.6, 
                marker=markers[index], linewidth=0)

    if index == 0:
        for x, y in zip(单机容量, 叶轮直径):
            if x != 3.85 and x != 6.45:
                if len(str(x)) == 3:
                        texts = [plt.text(x+0.02, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                          ha='left', va='bottom', fontsize=16,
                                          color = 'b', weight = 'semibold')]
                elif len(str(x)) == 4:
                        texts = [plt.text(x+0.02, y+0.2, '%.0f'%y+'-'+'%.2f'%x,
                                          ha='left', va='bottom', fontsize=16,
                                          color = 'b', weight = 'semibold')]
                else:
                        texts = [plt.text(x+0.02, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                          ha='left', va='bottom', fontsize=16,
                                          color = 'b', weight = 'semibold')]               
            text_list = text_list + texts

    elif index >= 3:
        for x, y in zip(单机容量, 叶轮直径):
            if y > 200:
                if len(str(x)) == 3:
                    texts = [plt.text(x+0.02, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                      ha='left', va='bottom', fontsize=16,
                                      alpha = 0.8)]
                elif len(str(x)) == 4:
                    texts = [plt.text(x+0.02, y+0.2, '%.0f'%y+'-'+'%.2f'%x,
                                      ha='left', va='bottom', fontsize=16,
                                      alpha = 0.8)]
                else:
                    texts = [plt.text(x+0.02, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                      ha='left', va='bottom', fontsize=16,
                                      alpha = 0.8)]
                    
#手动加text点
y_list = [173, 173, 172, 172, 171,
          175, 175, 175, 175,
          182, 183, 182, 182, 182, 183,
          187, 186, 185, 187, 185, 185,
          190, 190, 190, 190,
          192, 193, 193, 193, 193, 193, 192, 193,
          195, 195, 195,
          200, 200, 200, 200, 200, 200, 200, 200,
          216, 212
          ]
x_list = [3.6, 4, 6.25, 6.7, 6.7,
          3.35, 4.2, 5.5, 6.25,
          3.45, 3.65, 4, 4.65, 6.25, 6.5,
          4.55, 5, 5, 6.25, 6.25, 6.76,
          4.2, 5, 5.5, 6.25,
          4.2, 4.2, 4.5, 5, 5.56, 6.25, 6.5, 6.7,
          4.5, 5.5, 7.5,
          4.65, 5, 5.5, 6.7, 7.15, 7.5, 8, 8.5,
          8, 8.34
          ]
for x,y in zip(x_list, y_list):
    if len(str(x)) == 3: 
        texts = [plt.text(x+0.02, y+0.2, '%.0f'%y+'-'+'%.1f'%x, 
                 ha='left', va='bottom', fontsize=16, alpha = 0.8)]

    elif len(str(x)) == 4:
        texts = [plt.text(x+0.02, y+0.2, '%.0f'%y+'-'+'%.2f'%x, 
                 ha='left', va='bottom', fontsize=16, alpha = 0.8)]
'''
adjust_text(text_list,
            force_text=(2, 1),
            force_points=(0.2,3),
            #expand_points=(1.05,1.4),
            #expand_text=(1.5,1.2),
            arrowprops=dict(arrowstyle='-', color='black',lw=0.5),
            autoalign = 'x')  
'''
#legend
ax = fig1.gca()
ax.set_facecolor('whitesmoke')
ax.grid(ls = '--', alpha = 0.5)
plt.xlabel('单机容量（MW）')
plt.ylabel('叶轮直径（M）')
#added this to get the legend to work
handles,labels = ax.get_legend_handles_labels()
ax.legend(handles, labels = 厂商, loc='upper left', fontsize = 15)
#加单位功率扫风面积线
ylist = np.arange(3,8.5,0.5)
x = np.arange(2,11,1)
z_30 = (np.sqrt(3*x*1000/math.pi))*2
z_35 = (np.sqrt(3.5*x*1000/math.pi))*2
z_45 = (np.sqrt(4.5*x*1000/math.pi))*2
z_55 = (np.sqrt(5.5*x*1000/math.pi))*2
z_65 = (np.sqrt(6.5*x*1000/math.pi))*2
z_80 = (np.sqrt(8.0*x*1000/math.pi))*2
for y in ylist:
    z = (np.sqrt(y*x*1000/math.pi))*2
    plt.plot(x, z, color = 'darkgray', linewidth=1)
plt.fill_between(x, z_30, z_35, facecolor = 'purple', alpha = 0.1)
plt.fill_between(x, z_35, z_45, facecolor = 'red', alpha = 0.1)  
plt.fill_between(x, z_45, z_55, facecolor = 'blue', alpha = 0.1)
plt.fill_between(x, z_55, z_65, facecolor = 'green', alpha = 0.1)  
plt.fill_between(x, z_65, z_80, facecolor = 'orange', alpha = 0.1)

bbox_props = dict(boxstyle="square", fc="yellow", ec="0.5", alpha=0.8)
plt.text(4.6, 218, '8', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(5.3, 218, '7', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(6.2, 218, '6', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(7.4, 218, '5', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(8.9, 214, '4', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(8.9, 185, '3', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.xlim(3,9) 
plt.ylim(165,220)
plt.xticks(fontsize = 16)   
plt.yticks(fontsize = 16) 
plt.title('陆上竞品机型',fontweight = 'semibold', fontsize = 20)
plt.show()
# %% 海上机型谱
# set working directory
os.chdir('D:\\Personal\\Desktop\\国内国际市场洞察\\国内\\产品谱')
# %%%导入数据
data = pd.read_excel(r'.\\产品谱用.xlsx', sheet_name='海上')
data = data[(data['叶轮直径'] > 150) & (data['单机容量'] > 4)]
# %%%作图
fig1 = plt.figure(1,figsize=(24,18),dpi = 300)
# %%%散点图
colors = ['b','red','darkgreen','limegreen','magenta','darkorange','gold',
          'c','crimson','darkslategrey'
          ]
markers = ['s','d','^','v','*','^','v','o','o','.']
厂商 = ['金风','远景','明阳','明阳漂浮式','上海电气','海装','海装漂浮式',
      '东方电气','运达','哈电'
      ]
text_list = []
for index in range(10):
    单机容量 = data.loc[data['厂商'] == 厂商[index]]['单机容量']
    叶轮直径 = data.loc[data['厂商'] == 厂商[index]]['叶轮直径']
    plt.scatter(单机容量, 叶轮直径, 
                c=colors[index], cmap='brg', s=160, alpha=0.6, 
                marker=markers[index], linewidth=0)  
    if index == 0:
        for x, y in zip(单机容量, 叶轮直径):
            if y == 230 or y == 252:
                texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                  ha='left', va='top', fontsize=16,
                                  color = 'b', weight = 'semibold')]               
            else:                
                    if len(str(x)) == 3:
                        texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                          ha='left', va='bottom', fontsize=16,
                                          color = 'b', weight = 'semibold')]
                    elif len(str(x)) == 4:
                        if x < 10:
                            texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.2f'%x,
                                              ha='left', va='bottom', fontsize=16,
                                              color = 'b', weight = 'semibold')]
                        else:
                            texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.0f'%x,
                                              ha='left', va='bottom', fontsize=16,
                                              color = 'b', weight = 'semibold')]
            text_list = text_list + texts

    elif index == 1 or index == 2:
            for x, y in zip(单机容量, 叶轮直径):
                if x!= 5.0 and x != 5.2 and x!= 5.5 and x!=6.25 and x!= 6.45 and x != 8.5 and x!= 9.0 and y != 200:
                    if len(str(x)) == 3:
                        texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                          ha='left', va='bottom', fontsize=16,
                                          alpha = 0.8)]
                    elif len(str(x)) == 4:
                        if x < 10:
                            texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.2f'%x,
                                              ha='left', va='bottom', fontsize=16,
                                              alpha = 0.8)]
                        else:
                            texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.0f'%x,
                                              ha='left', va='bottom', fontsize=16,
                                              alpha = 0.8)]
                text_list = text_list + texts

    elif index <= 3:
        if index != 3:
            for x, y in zip(单机容量, 叶轮直径):
                if len(str(x)) == 3:
                    texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                      ha='left', va='bottom', fontsize=16,
                                      alpha = 0.8)]
                elif len(str(x)) == 4:
                    if x < 10:
                        texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.2f'%x,
                                          ha='left', va='bottom', fontsize=16,
                                          alpha = 0.8)]
                    else:
                        texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.0f'%x,
                                          ha='left', va='bottom', fontsize=16,
                                          alpha = 0.8)]
            text_list = text_list + texts
    else:
        for x, y in zip(单机容量, 叶轮直径):
            if y >270:
                texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                  ha='left', va='bottom', fontsize=16,
                                  alpha = 0.8)]
            text_list = text_list + texts

# %%%手动加text点
y_list = [155, 156, 158, 182, 203]
x_list = [5.5, 6.2, 7.25, 8.3, 11]
for x,y in zip(x_list, y_list):
    if x == 5.5:
        texts = [plt.text(x, y, '%.0f'%y+'-'+'%.1f'%x+'漂浮式', 
                 ha='right', va='top', fontsize=16, c='r')]
    elif x == 8.3:
        texts = [plt.text(x, y, '182-16.6漂浮式', 
                 ha='left', va='bottom', fontsize=16, c='r')]    
    else:
        if len(str(x)) == 4 and len(str(x)) < 10: 
            texts = [plt.text(x+0.1, y+0.1, '%.0f'%y+'-'+'%.2f'%x+'漂浮式', 
                     ha='left', va='top', fontsize=16, c='r')]
            text_list = text_list + texts
        else:
            texts = [plt.text(x+0.1, y+0.1, '%.0f'%y+'-'+'%.1f'%x+'漂浮式', 
                     ha='left', va='top', fontsize=16, c='r')]
       
'''
adjust_text(text_list,
            #force_text=(0.2, 0.5),
            #force_points=(0.3,0.6),
            #expand_points=(1.5,2),
            #expand_text=(1.1,1.2),
            arrowprops=dict(arrowstyle='-', color='black',lw=0.5))  
'''
# %%%legend
ax = fig1.gca()
ax.set_facecolor('whitesmoke')
ax.grid(ls = '--', alpha = 0.5)
plt.xlabel('单机容量（MW）')
plt.ylabel('叶轮直径（M）')
#added this to get the legend to work
handles,labels = ax.get_legend_handles_labels()
ax.legend(handles, labels = 厂商[:9], loc='upper left', fontsize = 15)
# %%%加单位功率扫风面积线
ylist = np.arange(2.5,6.5,0.5)
x = np.arange(2,21,1)
z_25 = (np.sqrt(2.5*x*1000/math.pi))*2
z_35 = (np.sqrt(3.5*x*1000/math.pi))*2
z_60 = (np.sqrt(6*x*1000/math.pi))*2
for y in ylist:
    if y == 3.5:
        x = np.arange(2,21,1)
        z = (np.sqrt(y*x*1000/math.pi))*2
        plt.plot(x, z, color = 'r', linewidth=1, alpha=0.7)
    else:
        x = np.arange(2,21,1)
        z = (np.sqrt(y*x*1000/math.pi))*2
        plt.plot(x, z, color = 'darkgray', linewidth=1, alpha=0.7)
plt.fill_between(x, z_25, z_35, facecolor = 'orange', alpha = 0.1)
plt.fill_between(x, z_35, z_60, facecolor = 'green', alpha = 0.1)   
        
bbox_props = dict(boxstyle="square", fc="yellow", ec="0.5", alpha=0.8)
plt.text(10.5, 283, '6', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(12.5, 283, '5', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(15.5, 283, '4', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(19.8, 277, '3', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(19.8, 256, '2.5', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.xlim(4,20)    
plt.ylim(150,285)
plt.xticks(fontsize = 16)   
plt.yticks(fontsize = 16) 
ax.yaxis.set_major_locator(MultipleLocator(15))
plt.title('海上竞品机型',fontweight = 'semibold', fontsize = 20)
plt.show()

# %% 国际陆上机型谱
#set working directory
os.chdir('D:\\Personal\\Desktop\\国内国际市场洞察\\国内\\产品谱')
#导入数据
data = pd.read_excel(r'.\\产品谱用.xlsx', sheet_name='国际陆上')
data = data[data['叶轮直径'] >= 150]
#作图
fig1 = plt.figure(1,figsize=(24,18),dpi=300)
#散点图
colors = ['b','slateblue','red','darkorange','green','magenta','c',
          'm','slategray','lightsteelblue','antiquewhite']
markers = ['s','s','d','^','v','*','p','.','.','.','.']
厂商 = ['金风科技','Vensys','远景','明阳','Vestas','SGRE','GE','Nordex',
      '运达','三一','上海电气']
text_list = []
for index in range(11):
    单机容量 = data.loc[data['厂商'] == 厂商[index]]['单机容量']
    叶轮直径 = data.loc[data['厂商'] == 厂商[index]]['叶轮直径']
    plt.scatter(单机容量, 叶轮直径, 
                c=colors[index], cmap='brg', s=160, alpha=0.6, 
                marker=markers[index], linewidth=0)  
    if index == 0 or index == 1:
        for x, y in zip(单机容量, 叶轮直径):
            if len(str(x)) == 3:
                texts = [plt.text(x, y, '%.0f'%y+'-'+'%.1f'%x,
                                  ha='left', va='bottom', fontsize=15,
                                  color = 'b', weight = 'semibold')]
            elif len(str(x)) == 4:
                texts = [plt.text(x, y, '%.0f'%y+'-'+'%.2f'%x,
                                  ha='left', va='bottom', fontsize=15,
                                  color = 'b', weight = 'semibold')]
            else:
                texts = [plt.text(x, y, '%.0f'%y+'-'+'%.1f'%x,
                                  ha='left', va='bottom', fontsize=15,
                                  color = 'b', weight = 'semibold')]               
            text_list = text_list + texts
    elif index <= 6:
        for x, y in zip(单机容量, 叶轮直径):
                if len(str(x)) == 3:
                    texts = [plt.text(x, y, '%.0f'%y+'-'+'%.1f'%x,
                                      ha='left', va='bottom', fontsize=15,
                                      alpha = 0.6)]
                elif len(str(x)) == 4:
                    texts = [plt.text(x, y, '%.0f'%y+'-'+'%.2f'%x,
                                      ha='left', va='bottom', fontsize=15,
                                      alpha = 0.6)]
                text_list = text_list + texts

'''
#手动加text点
y_list = []
x_list = []
for x,y in zip(x_list, y_list):
    if len(str(x)) == 3: 
        texts = [plt.text(x, y, '%.0f'%y+'-'+'%.1f'%x, 
                 ha='left', va='bottom', fontsize=12, alpha = 0.7)]
        text_list = text_list + texts
    elif len(str(x)) == 4:
        texts = [plt.text(x, y, '%.0f'%y+'-'+'%.2f'%x, 
                 ha='left', va='bottom', fontsize=12, alpha = 0.7)]
        text_list = text_list + texts   
'''
adjust_text(text_list,
            force_text=(0.2, 0.5),
            force_points=(0.3,0.6),
            expand_points=(1.5,2),
            expand_text=(1.1,1.2),
            arrowprops=dict(arrowstyle='-', color='black',lw=0.5),
            autoalign = 'y')  

#legend
ax = fig1.gca()
ax.set_facecolor('whitesmoke')
ax.grid(ls = '--', alpha = 0.5)
plt.xlabel('单机容量（MW）')
plt.ylabel('叶轮直径（M）')
#added this to get the legend to work
handles,labels = ax.get_legend_handles_labels()
ax.legend(handles, labels = 厂商[:7], loc='upper left', fontsize = 15)
#加单位功率扫风面积线
ylist = np.arange(2.5,7,0.5)
for y in ylist:
    x = np.arange(2,21,1)
    z = (np.sqrt(y*x*1000/math.pi))*2
    plt.plot(x, z, color = 'darkgray', linewidth=1, alpha=0.7)
bbox_props = dict(boxstyle="square", fc="yellow", ec="0.5", alpha=0.8)
plt.text(4.6, 194, '6.5', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(4.9, 194, '6', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(5.9, 194, '5', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(7.4, 194, '4', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(7.9, 174, '3', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(7.9, 158, '2.5', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.xlim(2.5,8)    
plt.ylim(145,195)
plt.xticks(fontsize = 16)   
plt.yticks(fontsize = 16) 
plt.title('国际陆上竞品机型',fontweight = 'semibold', fontsize = 20)
plt.show()
# %% 单个厂商机型谱
#导入数据
data = pd.read_excel(r'.\\作图用.xlsx')
#作图
#散点图
colors = ['b','red','darkorange','green','magenta','c']
厂商 = ['Vestas','SGRE','GE','Nordex','远景','运达','明阳','三一']
text_list = []
for index in range(8):
    fig = plt.figure(1,figsize=(24,14))
    单机容量 = data.loc[data['厂商'] == 厂商[index]]['单机容量']
    叶轮直径 = data.loc[data['厂商'] == 厂商[index]]['叶轮直径']
    技术路线 = data.loc[data['厂商'] == 厂商[index]]['技术路线']
    if 技术路线 == '双馈':
        plt.scatter(单机容量, 叶轮直径,
                c=colors[index], cmap='brg', s=130, alpha=0.6, 
                marker='^', linewidth=0) 
    elif 技术路线 == '鼠笼异步':
        plt.scatter(单机容量, 叶轮直径,
                c=colors[index], cmap='brg', s=130, alpha=0.6, 
                marker='o', linewidth=0) 
    elif 技术路线 == '中速永磁':
        plt.scatter(单机容量, 叶轮直径,
                c=colors[index], cmap='brg', s=130, alpha=0.6, 
                marker='s', linewidth=0)
    else:
        plt.scatter(单机容量, 叶轮直径,
                    c=colors[index], cmap='brg', s=130, alpha=0.6, 
                    marker='d', linewidth=0)
        
    for x, y in zip(单机容量, 叶轮直径):
        if y > 200:
            if len(str(x)) == 3:
                    texts = [plt.text(x, y, '%.0f'%y+'-'+'%.1f'%x,
                                      ha='left', va='bottom', fontsize=10)]
            elif len(str(x)) == 4:
                    texts = [plt.text(x, y, '%.0f'%y+'-'+'%.2f'%x,
                                      ha='left', va='bottom', fontsize=10)]
            text_list = text_list + texts
'''
#手动加text点
y_list = [171, 173, 173, 172, 172, 171,
          175, 175, 175, 175,
          182, 183, 182, 182, 182, 183,
          187, 186, 185, 187, 185, 185,
          190, 190, 190, 190,
          192, 193, 193, 193, 193, 193, 192, 193,
          195, 195, 195,
          200, 200, 200, 200, 200, 200, 200, 200
          ]
x_list = [3.5, 3.6, 4, 6.25, 6.7, 6.7,
          3.35, 4.2, 5.5, 6.25,
          3.45, 3.65, 4, 4.65, 6.25, 6.5,
          4.55, 5, 5, 6.25, 6.25, 6.76,
          4.2, 5, 5.5, 6.25,
          4.2, 4.2, 4.5, 5, 5.56, 6.25, 6.5, 6.7,
          4.5, 5.5, 7.5,
          4.65, 5, 5.5, 6.7, 7.15, 7.5, 8, 8.5
          ]
for x,y in zip(x_list, y_list):
    if len(str(x)) == 3: 
        texts = [plt.text(x, y, '%.0f'%y+'-'+'%.1f'%x, 
                 ha='left', va='bottom', fontsize=10)]
        text_list = text_list + texts
    elif len(str(x)) == 4:
        texts = [plt.text(x, y, '%.0f'%y+'-'+'%.2f'%x, 
                 ha='left', va='bottom', fontsize=10)]
        text_list = text_list + texts   
'''   
adjust_text(text_list,
            force_text=(1, 1),
            force_points=(1.5,5),
            expand_points=(1.1,1.2),
            arrowprops=dict(arrowstyle='-', color='black',lw=0.5))  
  
#legend
ax = fig1.gca()
ax.set_facecolor('whitesmoke')
ax.grid(ls = '--', alpha = 0.5)
plt.xlabel('单机容量（MW）')
plt.ylabel('叶轮直径（M）')
#added this to get the legend to work
handles,labels = ax.get_legend_handles_labels()
ax.legend(handles, labels = 厂商[:4], loc='upper left', fontsize = 15)
#加单位功率扫风面积线
ylist = np.arange(3,8.5,0.5)
for y in ylist:
    x = np.arange(2,11,1)
    z = (np.sqrt(y*x*1000/math.pi))*2
    plt.plot(x, z, color = 'darkgray', linewidth=1)
bbox_props = dict(boxstyle="square", fc="yellow", ec="0.5", alpha=0.8)
plt.text(4.2, 208, '8', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(4.8, 208, '7', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(5.6, 208, '6', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(6.7, 208, '5', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(8.4, 208, '4', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(8.9, 185, '3', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.xlim(3,9)    
plt.ylim(165,210)
plt.title('陆上竞品机型',fontweight = 'semibold', fontsize = 20)
plt.show()

# %% 海上机型谱extra
# %%%导入数据
data = pd.read_excel(r'.\\产品谱用.xlsx', sheet_name='Sheet1')
# %%%作图
fig1 = plt.figure(1,figsize=(24,18),dpi = 300)
# %%%散点图
colors = ['b','red','darkgreen','magenta','darkorange',
          'darkslategrey','maroon','orchid'
          ]
markers = ['s','d','^','*','^','p','h','o']
厂商 = ['金风','远景','明阳','上海电气','海装',
      '东方电气','运达','哈电'
      ]
text_list = []
for index in range(8):
    单机容量 = data.loc[data['厂商'] == 厂商[index]]['单机容量']
    叶轮直径 = data.loc[data['厂商'] == 厂商[index]]['叶轮直径']
    plt.scatter(单机容量, 叶轮直径, 
                c=colors[index], cmap='brg', s=160, alpha=0.6, 
                marker=markers[index], linewidth=0)  
    if index == 0:
        for x, y in zip(单机容量, 叶轮直径):
            if y == 230 or y == 252:
                texts = [plt.text(x+0.05, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                  ha='left', va='top', fontsize=16,
                                  color = 'b', weight = 'semibold')]               
            else:                
                    if len(str(x)) == 3:
                        texts = [plt.text(x+0.05, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                          ha='left', va='bottom', fontsize=16,
                                          color = 'b', weight = 'semibold')]
                    elif len(str(x)) == 4:
                        if x < 10:
                            texts = [plt.text(x+0.05, y+0.2, '%.0f'%y+'-'+'%.2f'%x,
                                              ha='left', va='bottom', fontsize=16,
                                              color = 'b', weight = 'semibold')]
                        else:
                            texts = [plt.text(x+0.05, y+0.2, '%.0f'%y+'-'+'%.0f'%x,
                                              ha='left', va='bottom', fontsize=16,
                                              color = 'b', weight = 'semibold')]
            text_list = text_list + texts
    elif index == 3:
            for x, y in zip(单机容量, 叶轮直径):
                if y!= 5.56:
                    if len(str(x)) == 3:
                        texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                          ha='left', va='bottom', fontsize=16,
                                          alpha = 0.8)]
                    elif len(str(x)) == 4:
                        if x < 10:
                            texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.2f'%x,
                                              ha='left', va='bottom', fontsize=16,
                                              alpha = 0.8)]
                        else:
                            texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.0f'%x,
                                              ha='left', va='bottom', fontsize=16,
                                              alpha = 0.8)]
                else:
                    if len(str(x)) == 3:
                        texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                          ha='left', va='top', fontsize=16,
                                          alpha = 0.8)]
                    elif len(str(x)) == 4:
                        if x < 10:
                            texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.2f'%x,
                                              ha='left', va='top', fontsize=16,
                                              alpha = 0.8)]
                text_list = text_list + texts      
    elif index == 7:
            for x, y in zip(单机容量, 叶轮直径):
                    if len(str(x)) == 3:
                        texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                          ha='left', va='top', fontsize=16,
                                          alpha = 0.8)]
                    elif len(str(x)) == 4:
                        if x < 10:
                            texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.2f'%x,
                                              ha='left', va='top', fontsize=16,
                                              alpha = 0.8)]
                        else:
                            texts = [plt.text(x+0.1, y+0.2, '%.0f'%y+'-'+'%.0f'%x,
                                              ha='left', va='top', fontsize=16,
                                              alpha = 0.8)]
         
    else: 
            for x, y in zip(单机容量, 叶轮直径):
                if len(str(x)) == 3:
                    texts = [plt.text(x+0.05, y+0.2, '%.0f'%y+'-'+'%.1f'%x,
                                      ha='left', va='bottom', fontsize=16,
                                      alpha = 0.8)]
                elif len(str(x)) == 4:
                    if x < 10:
                        texts = [plt.text(x+0.05, y+0.2, '%.0f'%y+'-'+'%.2f'%x,
                                          ha='left', va='bottom', fontsize=16,
                                          alpha = 0.8)]
                    else:
                        texts = [plt.text(x+0.05, y+0.2, '%.0f'%y+'-'+'%.0f'%x,
                                          ha='left', va='bottom', fontsize=16,
                                          alpha = 0.8)]
            text_list = text_list + texts

adjust_text(text_list,
            #force_text=(0.1, 3),
            #force_points=(0.3,0.6),
            #expand_points=(1.5,2),
            #expand_text=(1.1,1.2),
            arrowprops=dict(arrowstyle='-', color='black',lw=0.5))  
# %%%legend
ax = fig1.gca()
ax.set_facecolor('whitesmoke')
ax.grid(ls = '--', alpha = 0.5)
plt.xlabel('单机容量（MW）')
plt.ylabel('叶轮直径（M）')
#added this to get the legend to work
handles,labels = ax.get_legend_handles_labels()
ax.legend(handles, labels = 厂商[:8], loc='upper left', fontsize = 15)
# %%%加单位功率扫风面积线
ylist = np.arange(3,6.5,0.5)
for y in ylist:
    x = np.arange(2,21,1)
    z = (np.sqrt(y*x*1000/math.pi))*2
    plt.plot(x, z, color = 'darkgray', linewidth=1, alpha=0.7)
bbox_props = dict(boxstyle="square", fc="yellow", ec="0.5", alpha=0.8)

plt.text(10.5, 283, '6', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(12.5, 283, '5', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(15.5, 283, '4', ha='right', va='top', fontsize=15, bbox = bbox_props)
plt.text(19.8, 277, '3', ha='right', va='top', fontsize=15, bbox = bbox_props)

plt.xlim(4,20)    
plt.ylim(150,285)
plt.xticks(fontsize = 16)   
plt.yticks(fontsize = 16) 
ax.yaxis.set_major_locator(MultipleLocator(15))
plt.title('浙江海上投标机型',fontweight = 'semibold', fontsize = 20)
plt.show()
