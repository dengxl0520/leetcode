#
# @lc app=leetcode.cn id=1997 lang=python3
#
# [1997] 访问完所有房间的第一天
#

# @lc code=start
from typing import List

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0]*n
        # dp[0] = 1
        for i in range(1,n):
            dp[i] = (2*dp[i-1] +2 - dp[nextVisit[i-1]]) % (10**9+7)
        
        return dp[n-1]
    
    def firstDayBeenInAllRooms1(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        visited = [0] * n
        flag = 0
        curr_num = 0
        while flag != n:
            visited[curr_num] += 1
            if visited[curr_num] == 1:
                flag += 1
                
            if visited[curr_num] % 2 == 1:
                curr_num = nextVisit[curr_num]
            elif visited[curr_num] % 2 == 0:
                curr_num = (curr_num + 1) % n
        
        return int(sum(visited)-1 % (1e9 +7))
            
            
if __name__ == "__main__":
    nextVisit = [0,1,2,0]
    print(Solution().firstDayBeenInAllRooms(nextVisit))
# @lc code=end

