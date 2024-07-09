# @lcpr-before-debug-begin
from python3problem139 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30204
#
# [139] 单词拆分
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for j in range(len(s)+1):
            for i in range(len(wordDict)):
                if len(wordDict[i]) > j:
                    continue
                flag = True
                for k in range(len(wordDict[i])):
                    if wordDict[i][k] != s[j-len(wordDict[i])+k]:
                        flag = False
                if flag and dp[j-len(wordDict[i])]:
                    dp[j] = True
                    break
        
        return dp[-1]
                        


# @lc code=end



#
# @lcpr case=start
# "leetcode"\n["leet", "code"]\n
# @lcpr case=end
    
# @lcpr case=start
# "dogs"\n["dog","s","gs"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple", "pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats", "dog", "sand", "and", "cat"]\n
# @lcpr case=end

#

