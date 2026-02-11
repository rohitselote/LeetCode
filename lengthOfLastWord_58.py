class Solution(object):
    def lengthOfLastWord(self, s):
        w=s.strip().split()
        return len(w[-1])
