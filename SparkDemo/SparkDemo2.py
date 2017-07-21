# -*- coding:utf-8 -*-

import os
import sys

spark_path = "D:\ProgramFiles\Apache\spark-2.2.0-bin-hadoop2.6"

os.environ['SPARK_HOME'] = spark_path
os.environ['HADOOP_HOME'] = spark_path

sys.path.append(spark_path + "/bin")
sys.path.append(spark_path + "/python")
sys.path.append(spark_path + "/python/pyspark/")
sys.path.append(spark_path + "/python/lib")
sys.path.append(spark_path + "/python/lib/pyspark.zip")
sys.path.append(spark_path + "/python/lib/py4j-0.10.4-src.zip")

from pyspark import SparkContext
from pyspark import SparkConf

appName ="SparkDemo2"
master= "local"
conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)


data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)
res = distData.reduce(lambda a, b: a + b)
print (res)