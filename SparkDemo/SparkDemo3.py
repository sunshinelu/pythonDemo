# -*- coding:utf-8 -*-
from pyspark import SparkContext
from pyspark import SparkConf
import pyspark
import pyspark.sql
from pyspark.sql import SparkSession

master= "local"
#spark = SparkSession.builder.appName("SparkDemo3").master(master).getOrCreate()
# https://stackoverflow.com/questions/41353522/typeerror-builder-object-is-not-callable-spark-structured-streaming
spark = SparkSession.builder\
    .appName("SparkDemo3")\
    .master(master)\
    .getOrCreate()

# check spark version
print(spark.version)
