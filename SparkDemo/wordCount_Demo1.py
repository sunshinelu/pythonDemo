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
wordCounts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
# print(wordCounts.collect)
# wordCounts.saveAsTextFile("file:///D:\Workspace\PyCharm\pythonDemo\SparkDemo\wordCountDemo1_result.txt")
print(wordCounts.count())
wordCounts.saveAsTextFile("wordCountDemo1_result")