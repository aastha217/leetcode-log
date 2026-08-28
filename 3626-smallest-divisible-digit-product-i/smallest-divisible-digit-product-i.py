class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def digit_product(num):
            product = 1
            while num > 0:
                digit = num % 10
                product *= digit
                num = num // 10
            return product
        
        candidate = n
        while True:
            if digit_product(candidate) % t == 0:
                return candidate
            candidate += 1