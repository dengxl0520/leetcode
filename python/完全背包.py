
from typing import *


def package_complete(bagweight: int, weight: List, value: List):
    '''
        完全背包与01背包的区别是，每件物品的数量是无限的
        完全背包也可以使用贪心算法来做，以单位重量最高的顺序装满背包
    '''
    dp = [0] * (bagweight + 1)
    for i in range(len(weight)):
        for j in range(1, bagweight+1):
            if j >= weight[i]:
                dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
    return dp[-1]


if __name__ == "__main__":
    res = package_complete(4, [1,3,4], [15,20,30])
    print(res)