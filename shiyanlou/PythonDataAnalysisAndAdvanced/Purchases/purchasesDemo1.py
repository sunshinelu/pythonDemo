# -*- coding: utf-8 -*-
# purchasesDemo1



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

'''
解决字符编码问题
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 0: ordinal not in range(128)
参考链接：http://blog.sina.com.cn/s/blog_6c39196501013s5b.html
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 使用 Pandas 读取数据
df = pd.read_excel("user_fit.xlsx", header=0)

# 特征
x = df.iloc[:, 0:8]
x.head(5)

# 目标
y = df['用户是否为会员'.decode('utf-8')]

# 安装 3:7 切分验证集和训练集
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.3)

# 构建高斯贝叶斯分类器
model_GaussianNB = GaussianNB()

# 使用训练集训练模型
model_GaussianNB.fit(train_x, train_y)

# 使用验证集评估准确度
score = model_GaussianNB.score(test_x, test_y)

print(score)