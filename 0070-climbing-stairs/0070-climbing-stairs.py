class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        step1 = 2
        step2 = 1
        ways = 0
        for i in range(3, n+1):
            ways = step1+step2
            step2 = step1
            step1 = ways
        return ways