# -*- coding:utf-8 -*-
import sys
import os
import jieba
reload(sys)
sys.setdefaultencoding('utf-8')

#结巴分词--全模式
sent = '在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索空间树。'
wordlist = jieba.cut(sent, cut_all=True)
print " | ".join(wordlist)
#结巴分词--精确分词
wordlist2 = jieba.cut(sent)
print " | ".join(wordlist2)
#结巴分词--搜索引擎模式
wordlist3 = jieba.cut_for_search(sent)
print " | ".join(wordlist3)

print '载入词典后分析结果为：'
jieba.load_userdict("D:/Workspace/PyCharm/pythonDemo/datasets/userdict.txt")
sent2 = '在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索空间树。'
wordlist4 = jieba.cut(sent)#精确分词
print " | ".join(wordlist4)