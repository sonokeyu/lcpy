#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        v = 0
        for i in range(1, len(height)):
            left_max = max(height[0:i])
            right_max = max(height[i:len(height)])
            if height[i]<left_max and height[i]<right_max:
                v = v + min(left_max, right_max) - height[i]
        return v
# @lc code=end

