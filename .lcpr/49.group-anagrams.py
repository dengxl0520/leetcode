# @lcpr-before-debug-begin
from python3problem49 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30204
#
# [49] 字母异位词分组
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections
        mp = collections.defaultdict(list) # list作为元素

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st) # tuple可以作为key
        
        return list(mp.values())


    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        import collections
        mp = collections.defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())


    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        for i in range(len(strs)):
            # s = list(strs[i])
            # s.sort()
            # s = "".join(s)
            s = "".join(sorted(strs[i]))
            if s in d:
                res[d[s]].append(strs[i])
            else:
                d[s] = len(res)
                res.append([strs[i]])

        return res
# @lc code=end



#
# @lcpr case=start
# ["eat", "tea", "tan", "ate", "nat", "bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#

