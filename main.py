from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2 ** 31 - 1: return 0
        if x <= -2 ** 31: return 0

        if x < 0:
            y = y = str(x * -1)
        else:
            y = str(x)
        y = y[::-1]
        z = int(y)
        if z > 2147483647: return 0
        if z < -2147483648: return 0
        if x < 0: z *= -1
        return z


if __name__ == '__main__':
    print("test")

    print(Solution.reverse(Solution, 123))
