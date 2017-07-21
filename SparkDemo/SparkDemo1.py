# -*- coding:utf-8 -*-
'''
1, 从网站上下载spark
2, py4j和pyspark这两个库放到Python环境中，
'''
import os
os.environ['SPARK_HOME'] = r'D:\ProgramFiles\Apache\spark-2.2.0-bin-hadoop2.6'
from pyspark import SparkContext, SparkConf

appName ="jhl_spark_1" #你的应用程序名称
#Master URLs， 参见http://spark.apache.org/docs/latest/submitting-applications.html#master-urls
master= "local"
conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)

data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)
res = distData.reduce(lambda a, b: a + b)
print (res)