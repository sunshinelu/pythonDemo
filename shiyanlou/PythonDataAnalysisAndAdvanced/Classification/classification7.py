# -*- coding: UTF-8 -*-
# classification7－决策树

from sklearn.datasets import load_iris
from sklearn import tree

# 导入数据
iris = load_iris()

# 建立模型
model = tree.DecisionTreeClassifier()

# 模型训练
clf = model.fit(iris.data, iris.target)

import graphviz

dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)

graph.render("iris")