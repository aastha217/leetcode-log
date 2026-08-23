class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        half = n // 2
        
        # Calculate sum and count of '?' for the first half
        s1 = sum(int(c) for c in num[:half] if c != '?')
        cnt1 = num[:half].count('?')
        
        # Calculate sum and count of '?' for the second half
        s2 = sum(int(c) for c in num[half:] if c != '?')
        cnt2 = num[half:].count('?')
        
        # Bob wins if the mathematical balance holds true
        # Otherwise, Alice wins
        return 2 * (s1 - s2) != 9 * (cnt2 - cnt1)