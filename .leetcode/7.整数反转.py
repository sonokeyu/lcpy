#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # i = 0
        sum = 0
        flag = False
        if x < 0:
            x = -x
            flag = True
        while int(x/10):
            # print(sum * 10, int(x%10), sum, x%10)
            sum = sum * 10 + int(x%10)
            x = int(x/10)
        sum = sum * 10 + int(x%10)
        if  flag:
            if sum >= 2**31:
                return 0
            return -sum
        if sum >= 2**31 - 1:
                return 0
        return sum
# @lc code=end

