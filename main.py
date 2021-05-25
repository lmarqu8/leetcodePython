class Solution:
    def romanToInt(self, s: str) -> int:
        if s == "": return 0

        if s[0] == "M":
            if not s[1:]:
                return 1000
            else:
                return 1000 + self.romanToInt(self, s[1:])

        elif s[0] == "D":
            return 500 + self.romanToInt(self, s[1:])

        elif s[0] == "C":
            if not s[1:]:
                return 100

            elif s[1] == "D":
                return 400 + self.romanToInt(self, s[2:])

            elif s[1] == "M":
                return 900 + self.romanToInt(self, s[2:])

            else:
                return 100 + self.romanToInt(self, s[1:])

        elif s[0] == "L":
            return 50 + self.romanToInt(self, s[1:])

        elif s[0] == "X":
            if not s[1:]:
                return 10

            elif s[1] == "L":
                return 40 + self.romanToInt(self, s[2:])

            elif s[1] == "C":
                return 90 + self.romanToInt(self, s[2:])

            else:
                return 10 + self.romanToInt(self, s[1:])

        elif s[0] == "V":
            return 5 + self.romanToInt(self, s[1:])

        elif s[0] == "I":
            if not s[1:]:
                return 1

            elif s[1] == "V":
                return 4 + self.romanToInt(self, s[2:])

            elif s[1] == "X":
                return 9 + self.romanToInt(self, s[2:])

            else:
                return 1 + self.romanToInt(self, s[1:])


if __name__ == '__main__':
    x = "test"
    print(x)
    print(x[1:])

    print(Solution.romanToInt(Solution, "MMM"))
