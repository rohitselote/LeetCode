class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            s=str(x)
            if s==s[::-1]:
                return True
            else:
                return False
