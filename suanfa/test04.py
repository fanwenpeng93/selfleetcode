"""
剑指offer算法
"""

"""
两个栈实现一个队列：
"""
class queue:
    stack01=[]
    stack02=[]
    def __init__(self):
        pass
    def push(self,data):
        self.stack01.append(data)
    def pop(self):
        while len(self.stack01)!=0:
            self.stack02.append(self.stack01.pop())
        return self.stack02.pop()

"""
二进制中1的数量
"""
def erone(i):
    i=bin(i)
    count=0
    for i in str(i):
        if i=="1":
            count=count+1
    print(count)
    return count
"""
输入x，y，求x的y次方
"""
class Solution:
    def Power(self, base, exponent):
        # write code here
        try:
            if exponent >= 0:
                return self.Power_value(base, exponent)
            else:
                return 1/self.Power_value(base, abs(exponent))
        except:
            print('base == zero')

    def Power_value(self, base, exponent):
        if exponent == 1:
            return base
        elif exponent == 0:
            return 1
        else:
            while exponent>0:
                v=v*base
            return v

"""
奇数放在偶数前面
"""
def jo(l):
    pass

"""
二叉树镜像，即左右反转
"""
def rechashujx(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return root
    root.left,root.right=root.letf,root.right
    rechashujx(root.letf)
    rechashujx(root.letf)
    return root

"""
数组中出现次数超过一半的数字：1，暴力法 2、这个数字在列表的中间
"""
def lnum(l):
    l.sort()
    mid=int(len(l)/2)
    print(mid)
    n=l[mid]
    cizhu=l.count(n)
    if cizhu>int(len(l)/2):
        print(cizhu)
"""
求列表中是否有两数字相加等于目标值
"""

def mubiaohe(l,target):
    before=0
    after=len(l)-1
    l.sort()
    while before<after:
        if l[before]+l[after]>target:
            after=after-1
        elif l[before]+l[after]<target:
            before=before+1
        elif l[before]+l[after]==target:
            return (l[before],l[after])

"""
最长公共子串
"""