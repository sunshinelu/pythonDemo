# -*- coding: UTF-8 -*-
# classification8－随机森林 VS. 决策树

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# 导入数据
iris = load_iris()

x_train = iris.data[:120]
x_test = iris.data[120:]

y_train = iris.target[:120]
y_test = iris.target[120:]

# 建立模型
model_tree = DecisionTreeClassifier(random_state=10)
model_random = RandomForestClassifier(random_state=10)

# 训练模型并验证
model_tree.fit(x_train, y_train)
s1 = model_tree.score(x_test, y_test)

model_random.fit(x_train, y_train)
s2 = model_random.score(x_test, y_test)

print('DecisionTree:', s1)
print('RandomForest:', s2)