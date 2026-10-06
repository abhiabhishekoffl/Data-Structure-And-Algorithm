from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) < 3:
            return []

        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return [list(triplet) for triplet in result]


if __name__ == "__main__":
    s = Solution()
    # The set does not preserve order, so results are sorted only for printing.
    print(sorted(s.threeSum([-1, 0, 1, 2, -1, -4])))  # [[-1, -1, 2], [-1, 0, 1]]
    print(sorted(s.threeSum([0, 1, 1])))              # []
    print(sorted(s.threeSum([0, 0, 0])))              # [[0, 0, 0]]