class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        i=0
        n=len(s)
        while i<n-1:
            result+=s[i]+chr(ord(s[i])+int(s[i+1]))
            i+=2
        if n%2!=0:
            result+=s[-1]
        return result