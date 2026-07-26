class Solution:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        ans = 0

        for i in range(n):
            left = i + 1
            right = n - i

            total = left * right
            odd = (total + 1) // 2

            ans += arr[i] * odd

        return ans