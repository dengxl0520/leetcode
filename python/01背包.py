
from typing import *

def package_01(bagweight: int, weight: List, value: List) -> int:
    n = len(weight) # n件物品
    
    dp = [[0] * (bagweight+1) for _ in range(n)] # dp[i][j], 第i个物品(n), j重量(bagweight+1)
    # dp初始化
    # 初始化第0号物品，当背包容量大于0号物品重量时，放入0号物品
    for i in range(weight[0], bagweight+1):
        dp[0][i] = value[0]

    # dp[i][j] 表示 0-i的物品任意取，放进容量j的背包，价值总和最大
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            # 状态转移方程
            # 不放第i个物品，就是dp[i-1][j]
            # 放第i个物品，就是dp[i-1][j-weight[i]] + value[i]
            # dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
            # 还要判断j-weight[i]有没有越界
            if j - weight[i] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]
    

if __name__ == "__main__":
    res = package_01(15, weight=[1,1,2,4,12], value=[1,2,2,10,4])
    # res = package_01(4, weight=[1,3,4], value=[15,20,30])
    print(res)