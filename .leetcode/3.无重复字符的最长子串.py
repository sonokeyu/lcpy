#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = []
        temp_len = 0
        if not len(s):
            print("??")
            return 0
        max_len = 1
        for i in s:
            if i not in hash_map:
                hash_map.append(i)
                temp_len += 1
            else:
                max_len = max_len if max_len>temp_len else temp_len
                temp_len = 1
                hash_map.clear()
                hash_map.append(i)
        max_len = max_len if max_len>temp_len else temp_len
        return max_len

# @lc code=end

