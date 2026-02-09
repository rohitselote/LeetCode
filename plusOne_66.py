class Solution(object):
    def plusOne(self, digits):
        if digits[-1]!=9:
            digits[-1] = digits[-1]+1
        else:
            i=len(digits)-1 
            while digits[i]==9 and i>=0: 
                digits[i]=0
                i=i-1
            if i<0:
                return [1]+digits
            digits[i]+=1
        return digits
