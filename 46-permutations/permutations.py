class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [] #step1
        n = len(nums)
        if n == 1: #step 2
            return [[nums[0]]]
        for i in range(n): #step 3
            v = nums.pop(i) #step 4
            perm = self.permute(nums)
            for each in perm: #step 5 
                each.append(v)
            res += perm #step 6
            nums.insert(i,v) #step 7
        return res