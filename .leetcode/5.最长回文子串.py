#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        start = 0
        end = 0
        if len(s) == 1:
            return s
        else:
            for i in range(len(s)-1):
                # 以s[i]为中点的奇数长度回文串
                temp_len = 0
                # print(s[i])
                while temp_len < i and i + temp_len + 2 <= len(s) and s[i-temp_len-1] == s[i+temp_len+1]:
                    # print("enter odd with lenth", temp_len)
                    temp_len += 1
                if 2 * temp_len + 1 > max_len:
                    max_len = 2 * temp_len + 1
                    start = i - temp_len
                    end = i + temp_len
                    # print("update odd", s[start:end+1])
                # 以s[i]、s[i+1]为中点的偶数长度的回文串
                if s[i] == s[i+1]:
                    temp_len = 1
                    # print("enter even")
                    flag_even = True
                    while temp_len - 1 < i and i + temp_len + 2 <= len(s) and s[i-temp_len] == s[i+temp_len+1]:
                        # print("enter even with lenth", temp_len)
                        temp_len += 1
                    if flag_even and 2 * temp_len > max_len:
                        max_len = 2 * temp_len
                        start = i - temp_len + 1
                        end = i + temp_len
                        # print("update even", s[start:end+1])
            return s[start:end+1]
if __name__ == '__main__':
    q = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    a = Solution()
    w = a.longestPalindrome(q)
    print("final", w)
# @lc code=end

