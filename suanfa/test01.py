"""
主要是排序
"""

'''
冒泡排序
'''
def maopao(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

'''
快速排序
'''
def quit(l):
    if len(l)<2:
        return l
    else:
        m=l[0]
        left=[i for i in l[1:] if i<=m]
        right=[j for j in l[1:] if j>m]
        return quit(left)+[m]+quit(right)

'''
选择排序
'''
def select(l):
    for i in range(len(l)-1):
        minone=i
        for j in range(i,len(l)):
            if l[minone]>l[j]:
                minone=j
        l[i],l[minone]=l[minone],l[i]
    return l

'''
插入排序???
'''
def insert(l):
    for i in range(len(l)-1):
        minone=i
        for j in range(i,len(l)):
            if l[minone]>l[j]:
                minone=j
        for n in range(i,minone):
            l[n+1]=l[n]
        l[i]=l[minone]
    return l



if __name__=="__main__":
    l=[8,9,6,1,92,56]


    print(insert(l))


