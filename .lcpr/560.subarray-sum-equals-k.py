#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30204
#
# [560] 和为 K 的子数组
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
            当遍历到nums[i]时，
        '''
        from collections import defaultdict
        ans = s = 0
        cnt = defaultdict(int)
        cnt[0] = 1  # s[0]=0 单独统计
        for x in nums:
            s += x
            ans += cnt[s - k]
            cnt[s] += 1
        return ans

    def subarraySum1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            sum = 0
            for j in range(i,n):
                sum += nums[j]
                if sum == k:
                    res += 1
        return res
# @lc code=end



#
# @lcpr case=start
# [1,-1,0]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#

