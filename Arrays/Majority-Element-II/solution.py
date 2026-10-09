from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        result = []

        for key, value in hashmap.items():
            if value > n // 3:
                result.append(key)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))                 # [3]
    print(s.majorityElement([1]))                       # [1]
    print(s.majorityElement([1, 2]))                    # [1, 2]
    print(s.majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))  # [1, 2]
    print(s.majorityElement([1, 2, 3, 4, 5, 6]))        # []