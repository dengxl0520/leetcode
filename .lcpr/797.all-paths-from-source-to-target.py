# @lcpr-before-debug-begin
from python3problem797 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=797 lang=python3
# @lcpr version=30204
#
# [797] 所有可能的路径
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) -1
        res = []
        path = [0]
        def dfs(point):
            if point == target:
                res.append(path[:])
                return

            for i in graph[point]:
                path.append(i)
                dfs(i)
                path.pop()
        dfs(0)
        return res

# @lc code=end



#
# @lcpr case=start
# [[1,2],[3],[3],[]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,3,1],[3,2,4],[3],[4],[]]\n
# @lcpr case=end

#

