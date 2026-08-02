class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        max_len0s,max_len1s=0,0
        i=0
        n=len(s)
        while i<n:
            len0s,len1s=0,0
            while i<n and s[i]=='0':
                len0s+=1
                i+=1
            while i<n and s[i]=='1':
                len1s+=1
                i+=1
            if max_len0s<len0s:
                max_len0s=len0s
            if max_len1s<len1s:
                max_len1s=len1s
        return max_len1s>max_len0s