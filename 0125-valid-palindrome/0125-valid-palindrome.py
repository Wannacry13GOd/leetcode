class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = "".join(i.lower() for i in s if i.isalnum())
        return res == res[::-1]