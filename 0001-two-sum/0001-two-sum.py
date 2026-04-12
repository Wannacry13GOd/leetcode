class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}

        for i, num in enumerate(nums):
            compl = target - num
            if compl in num_dict:
                return [num_dict[compl], i]
            num_dict[num] = i
        return[]