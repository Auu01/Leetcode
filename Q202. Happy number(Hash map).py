class Solution:
    def isHappy(self, n: int) -> bool:
        def squares(num):
            total_sum = 0
            while num > 0:
                digit = num % 10
                total_sum += digit ** 2
                num = num // 10
            return total_sum

        seen = {}
        while n != 1 and n not in seen:
            seen[n] = True
            n = squares(n)
        return n == 1
