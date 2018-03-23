# -*- coding: utf-8 -*-

"""
参考链接：

python初步实现word2vec：http://blog.csdn.net/xiaoquantouer/article/details/53583980
Google Word2vec 学习手札: http://blog.csdn.net/MebiuW/article/details/52295138
"""
import sys
import chardet
import re

text_path = "/Users/sunlu/Documents/数据集/搜狗实验室/搜狐新闻数据(SogouCS)/news_sohusite_xml.smarty.dat"
f = open(text_path,'r')


# data = f.read()
# print chardet.detect(data)

# line1 = f.readline().decode('utf-8')
# print line1

line2 = f.readlines()
f2 = open("news_sohusite.txt", 'w')
for l in line2:
     # print l.decode('gb2312', 'ignore')

    # compile提高正则匹配效率
    reg = re.compile(r'<content>(.*?)</content>')
    # 返回list列表
    items = re.findall(reg, l.decode('gb2312', 'ignore').encode("utf-8"))
    for item in items:
        print item
        if len(item) >= 4 :
            f2.write(item + '\n')


