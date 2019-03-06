#!/usr/bin/env python
# coding: utf-8

# In[243]:


#https://www.itread01.com/content/1542564499.html Plotly初步
import pandas as pd
sht = pd.read_excel(r'D:/Study/Python/Project/Python3/PratXlwings/y07-03-O.xls',
                    encoding='big5',
                    sheet_name =2, #第二個sheet
                    index_col =0, #左邊數來第2個當index
                    header=1 #上面數來第1個當作標頭
                   )
DF=pd.DataFrame(sht) #將讀出的資料轉成 DataFrame
DF


# In[244]:


# 把原本NaN用 fillna 補起來 
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html
ww=DF.fillna(method ='pad', #複製前面的值填空
             axis =1 # 0 or ‘index’, 1 or ‘columns’
            ) 
ww


# In[245]:


# DF.iloc[1:26,0:59]  #切割，取索引列 1 到 26 ,列 0 到 28 
# DF.iloc[1:26,'Unnamed: 1':'Unnamed: 58']  


# In[246]:


import plotly.plotly
import plotly.graph_objs as go
# ww.T.iloc[0,3:25] # T轉置後 使用iloc會變成取 ww的行， [0,3:25] 表示取 0行中的index 3:25 
# aa=ww.iloc[0,3:58].values  #取ww的列
aa=ww.iloc[0,1]+ww.iloc[1,1]
aa


# In[247]:


# y=ww.T.iloc[0,2:]
y=ww.T.iloc[0,2:]
y


# In[248]:


ww.iloc[0,2:]


# In[249]:


len(ww.iloc[0])


# In[250]:


ww


# In[273]:


import seaborn as sns
from matplotlib import colors

data =[]
col = 2 #從第 2+1 行開始
row =2 #從第 2+1 列開始
cout = 0
Colorss = [{'color': colors.rgb2hex(i)} for i in sns.color_palette('Set2',len(ww.iloc[0,col:])) ] #定意圖型顏色，依照國家男女區分56個

#https://zhuanlan.zhihu.com/p/27471537 (調整 sns.color_palette 可參考左邊網址 )


# In[275]:


#https://www.cnblogs.com/feffery/p/9293745.html (更多plotly圖表設定可參考左邊)
# print(Colorss,len(Colorss))
for _ in ww.iloc[0,col:]: #
#     print(cout,Colorss[1])
    trace = go.Bar(
        x=ww.T.iloc[0,row:].index, # ww.T.iloc[0,row:] 求第0行，列從row到底
        y=ww.T.iloc[col,row:],
        name=ww.iloc[0,col]+ww.iloc[1,col], #定義名稱
        marker= Colorss[cout]    #定義顏色，順著每一行定義顏色
    )
#     print(cout,Colorss[cout])
    data.append(trace)
    col=col+1
    cout =cout+1    
# print(data)
layout = go.Layout(barmode='stack',
                   title='Foreign Resident by Nationality & Occupation ',
                   plot_bgcolor = "rgb(223, 232, 243)", #背景顏色
#                     xaxis=dict(
#                         title='x Axis',
#                         titlefont=dict(
#                             family='Courier New, monospace',
#                             size=18,
#                             color='#7f7f7f'
#                         )
#                     ),
                    yaxis=dict(
                        title='Number of People',
                        titlefont=dict(
                            family='Courier New, monospace',
                            size=18,
#                             color='#7f7f7f'
                        )
                    )
                  )
output_path = "D:\Study\Python\Project\Python3\PratXlwings\OccupOutput.html"    
fig=go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename=output_path)


# In[ ]:





# In[ ]:




