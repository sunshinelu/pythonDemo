#-*- coding: utf-8 -*-

# http://spaces.ac.cn/archives/3360/

import numpy as np #导入numpy
import pandas as pd
import jieba

def yuchuli(s,m): #导入文本，文本预处理
	wenjian = pd.read_csv(s, delimiter='     xxx     ', encoding='utf-8', \
	header= None, names=['comment']) #导入文本
	wenjian = wenjian['comment'].str.replace('(<.*?>.*?<.*?>)','').str.replace('(<.*?>)','')\
	.str.replace('(@.*?[ :])',' ') #替换无用字符
	wenjian = pd.DataFrame({'comment':wenjian[wenjian != '' ]})
	wenjian.to_csv('out_'+s, header=False, index=False)
	wenjian['mark'] = m #样本标记
	return wenjian.reset_index()

neg = yuchuli('data_neg.txt',-1)
pos = yuchuli('data_pos.txt',1)

mydata = pd.concat([neg,pos],ignore_index=True)[['comment','mark']] #结果文件
#预处理基本结束



#开始加载情感词典
negdict = [] #消极情感词典
posdict = [] #积极情感词典
nodict = [] #否定词词典
plusdict = [] #程度副词词典
sl = pd.read_csv('dict/neg.txt', header=None, encoding='utf-8')
for i in range(len(sl[0])):
	negdict.append(sl[0][i])
sl = pd.read_csv('dict/pos.txt', header=None, encoding='utf-8')
for i in range(len(sl[0])):
	posdict.append(sl[0][i])
sl = pd.read_csv('dict/no.txt', header=None, encoding='utf-8')
for i in range(len(sl[0])):
	nodict.append(sl[0][i])
sl = pd.read_csv('dict/plus.txt', header=None, encoding='utf-8')
for i in range(len(sl[0])):
	plusdict.append(sl[0][i])
#加载情感词典结束


#预测函数

