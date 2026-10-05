from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_elements = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in seen_elements:
                return [seen_elements[needed], i]

            seen_elements[nums[i]] = i