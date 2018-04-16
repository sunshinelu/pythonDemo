# -*- coding:utf-8 -*-
from pyspark import SparkContext
from pyspark import SparkConf
import pyspark
import pyspark.sql
from pyspark.sql import SparkSession

master= "local"
spark = SparkSession.builder\
    .appName("SparkDemo3")\
    .master(master)\
    .getOrCreate()

sc = spark.sparkContext

text_file = sc.textFile("file:///D:\Workspace\PyCharm\pythonDemo\SparkDemo\wordCountDemo1.txt")
def splitChar(x):
    result = ""
    for i in x:
        result = result + " " + i
    return result

wordCounts = text_file.map(lambda x: splitChar(x)).flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
# print(wordCounts.collect)
# wordCounts.saveAsTextFile("file:///D:\Workspace\PyCharm\pythonDemo\SparkDemo\wordCountDemo1_result.txt")
print(wordCounts.count())
wordCounts.saveAsTextFile("wordCountDemo2_result")