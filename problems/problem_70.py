# 70. Climbing Stairs
#
# You are climbing a staircase. It takes n steps to reach the top. Each time you
# can either climb 1 or 2 steps. In how many distinct ways can you climb to the
# top?
#
# Constraints:
#
# - 1 <= n <= 45


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.__fibonacci(n + 1)

    def __fibonacci(self, n: int) -> int:
        a, b = 0, 1

        for i in range(0, n):
            a, b = b, a + b

        return a
