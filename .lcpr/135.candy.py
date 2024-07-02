#
# @lc app=leetcode.cn id=135 lang=python3
# @lcpr version=30204
#
# [135] 分发糖果
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1
            
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candy[i-1] = max(candy[i-1], candy[i] + 1) 
        
        return sum(candy)
    
    def candy1(self, ratings: List[int]) -> int:
        '''
            硬模拟，出不来
        '''
        if len(ratings) < 2:
            return len(ratings)
        
        res = [0] * len(ratings)
        
        for i in range(1, len(ratings)-1):
            if ratings[i-1] > ratings[i] and ratings[i] < ratings[i-1]:
                res[i] = 1
                # left
                left = i - 1
                while left > 1 and left < len(ratings)-1:
                    if ratings[left] > ratings[left+1]:
                        res[left] = res[left+1] + 1
                    else:
                        break
                    left -= 1
                # right
                right = i + 1
                while right > 1 and right < len(ratings)-1:
                    if ratings[right-1] < ratings[right]:
                        res[right] = res[right-1] +1
                    else:
                        break
                    right += 1
                
        if res[0] == 0: res[0] = 1
        for i in range(1, len(res)):
            if ratings[i-1] < ratings[i]:
                res[i] = res[i-1] + 1
            else:
                break
        if res[-1] == 0: res[-1] = 1
        for i in range(len(res)-2, -1, -1):
            if ratings[i-1] > ratings[i]:
                res[i-1] = res[i] + 1
            else:
                break

        for i in range(len(res)):
            if res[i] == 0:
                pass
            
        
        
# @lc code=end



#
# @lcpr case=start
# [1,0,3,2,4,1,2,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

#

