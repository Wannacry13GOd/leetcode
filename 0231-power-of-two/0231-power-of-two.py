class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        base = 2
        power = 0
        while base ** power < n:
            power+=1
        return base ** power == n