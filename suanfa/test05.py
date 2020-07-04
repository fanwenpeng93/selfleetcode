"""
动态规划
"""

"""
简单的动态规划：每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""
def palou(n):
    if n<=2:
        return n
    dp=[0,1,2]
    for i in range(3,n+1):
        temp=dp[i-1]+dp[i-2]
        dp.append(temp)
    return dp[i]
"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4

思路：
dp[i]=max(dp[i-1],dp[i-2]+nums[i])
"""
def xiaotou(nums):
    if len(nums) == 0:
        return 0
    if len(nums) <= 2:
        return max(nums)
    dp=[]
    dp.append(nums[0])
    dp.append(max(nums[0],nums[1]))
    nowmax=max(dp[0],dp[1])
    for i in range(2,len(nums)):
        temp=max(dp[i-1],dp[i-2]+nums[i])
        dp.append(temp)
        if dp[i]>nowmax:
            nowmax=dp[i]
    return nowmax





