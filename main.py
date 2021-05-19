from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        vals = []

        size = len(nums)

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i != j:
                    if target - nums[i] == nums[j]:
                        vals.append(i)
                        vals.append(j)

            if len(vals) == 2: break

        return vals


if __name__ == '__main__':
    print("test")

    nums = [2, 7, 11, 15]
    target = 9

    print(Solution.twoSum(Solution, nums, target))
