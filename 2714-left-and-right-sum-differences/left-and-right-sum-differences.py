class Solution:
    def leftRightDifference(self, nums):

        total = sum(nums)
        left = 0
        answer = []

        for num in nums:
            total -= num
            answer.append(abs(left - total))
            left += num

        return answer