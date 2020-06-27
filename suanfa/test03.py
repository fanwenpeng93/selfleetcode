"""
主要是字符串算法
"""

"""
you ar good 反转单词顺序
"""

def a01(s):
    l=s.split(" ")
    l.reverse()
    s=" ".join(l)
    print(s)
    return s
"""
把字符串 s 中的每个空格替换成"%20"
"""
s=""
s.replace(" ","%20")
def a02(s):
    l=s.split(" ")
    l.reverse()
    s="%20".join(l)
    print(s)
    return s

"""
1个字符串中最长的无重复子序列
"""
