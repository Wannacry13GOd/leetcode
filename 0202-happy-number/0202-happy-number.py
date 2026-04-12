class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            digits = [int(x) for x in str(n)]
            n = sum(i * i for i in digits)
        return n == 1