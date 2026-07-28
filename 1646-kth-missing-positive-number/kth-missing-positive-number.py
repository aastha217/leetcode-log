class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        for x in arr:
            if x <= k:
                k += 1
            else:
                break
        return k