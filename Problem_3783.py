class Solution(object):
    def mirrorDistance(self, n):

        arr=str(n)
        arr2=arr[::-1]
        m=int(arr2)
        return abs(n-m)
