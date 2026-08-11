class Solution:
    def maximizeSum(self, nums, k):
        j = max(nums)
        i = 0
        while k > 0:
            i += j
            j += 1
            k -= 1
        return i