# @before-stub-for-debug-begin
from python3problem904 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = DefaultDict(int)
        tot, slow = 0, 0
        ans = 0
        for i in range(len(fruits)):
            cnt[fruits[i]] += 1
            if cnt[fruits[i]] == 1:
                tot += 1
            while tot > 2:
                cnt[fruits[slow]] -= 1
                if cnt[fruits[slow]] == 0:
                    tot -= 1
                slow += 1
            if i - slow + 1 > ans:
                ans = i - slow + 1
        print(ans)
        return ans
        
        
    def totalFruit1(self, fruits: List[int]) -> int:
        fast, slow = 0,0
        cur_fruit = []
        max_num = 0
        while fast < len(fruits):
            if fruits[fast] not in cur_fruit:
                if len(cur_fruit) < 2:
                    cur_fruit.append(fruits[fast])
                else:
                    new_slow = fast -2
                    while fruits[fast-1] == fruits[new_slow]:
                        new_slow -= 1
                    cur_fruit.remove(fruits[new_slow])
                    slow = new_slow +1
                    cur_fruit.append(fruits[fast])
            num = fast - slow + 1
            if num > max_num:
                max_num = num # max_num = max(num, max_num)
            fast += 1
        print(fruits, max_num)
        return max_num
# @lc code=end

