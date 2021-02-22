#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
# @lc code=end


if __name__ == '__main__':
    print("1")
    hashmap={}
    nums = [0, 2, 7, 6, 3]
    target = 9
    for ind,num in enumerate(nums):
        print(ind,num)
        hashmap[num] = ind
    print(hashmap)
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            print([i,j])