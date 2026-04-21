class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for x in nums:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        return max(counts, key=counts.get)