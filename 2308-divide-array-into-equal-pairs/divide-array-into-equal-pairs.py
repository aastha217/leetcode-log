class Solution(object):
    def divideArray(self, nums):
        from collections import Counter
        c = Counter(nums)
        for v in c.values():
            if v % 2:
                return False
        return True