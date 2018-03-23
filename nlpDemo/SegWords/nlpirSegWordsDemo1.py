# -*- coding: utf-8 -*-

"""
参考链接：

自己动手做聊天机器人 十-半个小时搞定词性标注与关键词提取:
http://www.shareditor.com/blogshow/?blogId=74
"""

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import pynlpir

pynlpir.open()
s = '聊天机器人到底该怎么做呢？'
segments = pynlpir.segment(s)
for segment in segments:
    print segment[0], '\t', segment[1]

pynlpir.close()