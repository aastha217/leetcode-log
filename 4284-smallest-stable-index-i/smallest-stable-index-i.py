class Solution(object):
    def firstStableIndex(self, nums, k):
        for j in range(len(nums)):
            x = nums[0:j+1]
            y = nums[j:len(nums)]
            score = max(x) - min(y)
            if score <= k:
                return j

        return -1

        