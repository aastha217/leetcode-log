class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        arr =[]

        for i in range(len(str(n))):
            arr.append(str(n)[i])     
        arr.sort()
        if len(arr) == 1:
            return arr[-1]
        else:
            return int(arr[-1])*(int(arr[-2]))    
