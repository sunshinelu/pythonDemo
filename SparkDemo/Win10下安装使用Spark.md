
设置`HADOOP_HOME`，将winutils.exe放置在`HADOOP_HOME\bin`目录下，使用管理员权限执行如下命令：

    C:\hadoop\bin\winutils.exe chmod 777 C:\tmp\hive

查看`C:\hadoop\bin\winutils.exe ls -F C:\tmp\hive`运行情况，则输入以下命令：

     C:\hadoop\bin\winutils.exe ls C:\tmp\hive
    drwxrwxrwx 1 SUNLU\sunlu SUNLU\None 0 Jul 21 2017 C:\tmp\hive


参考链接：
https://stackoverflow.com/questions/34196302/the-root-scratch-dir-tmp-hive-on-hdfs-should-be-writable-current-permissions

### 报错：java.io.IOException: Could not locate executable D:\ProgramFiles\Apache\spark-2.2.0-bin-hadoop2.6\bin\winutils.exe in the Hadoop binaries.

将winutils.exe放入D:\ProgramFiles\Apache\spark-2.2.0-bin-hadoop2.6\bin目录下即可。

### 报错：TypeError: 'str' object is not callable
Traceback (most recent call last):
  File "D:/Workspace/PyCharm/pythonDemo/SparkDemo/SparkDemo3.py", line 14, in <module>
    spark.version()
TypeError: 'str' object is not callable

    spark.version()

修改为：

    spark.version
    
运行正常！

参考链接：
https://stackoverflow.com/questions/23691532/python-3-4-typeerror-str-object-is-not-callable


### 报错：TypeError: 'Builder' object is not callable
Traceback (most recent call last):
  File "D:/Workspace/PyCharm/pythonDemo/SparkDemo/SparkDemo3.py", line 11, in <module>
    spark = SparkSession.builder()\
TypeError: 'Builder' object is not callable

    spark = SparkSession.builder()\
        .appName("SparkDemo3")\
        .getOrCreate()
        
修改为：

    spark = SparkSession.builder\
    .appName("SparkDemo3")\
    .getOrCreate()
    
后，运行正常！

参考链接：
https://stackoverflow.com/questions/41353522/typeerror-builder-object-is-not-callable-spark-structured-streaming


使用PyCharm配置Spark的Python开发环境，参考链接：
http://blog.tomgou.xyz/shi-yong-pycharmpei-zhi-sparkde-pythonkai-fa-huan-jing.html