# 15. 3Sum

**Difficulty:** Medium
**Link:** [LeetCode - 3Sum](https://leetcode.com/problems/3sum/description/)
**Pattern:** Sorting + Two Pointers

## Problem

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`, `i != k` and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must **not contain duplicate triplets**. The triplets and their order in the output can be in any order.

### Examples

| Input | Output | Explanation |
|-------|--------|-------------|
| `nums = [-1,0,1,2,-1,-4]` | `[[-1,-1,2],[-1,0,1]]` | `-1 + -1 + 2 = 0` and `-1 + 0 + 1 = 0` |
| `nums = [0,1,1]` | `[]` | The only possible sum is `2`, not `0` |
| `nums = [0,0,0]` | `[[0,0,0]]` | `0 + 0 + 0 = 0` |

### Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Approach

1. **Brute force:** Use three nested loops to check every combination of three numbers. It is simple, but it takes **O(n³)** time, which is too slow for `n = 3000`.

2. **Optimized (Sorting + Two Pointers):**
   - If `nums` has fewer than 3 elements, return `[]`.
   - Sort `nums` in place with `nums.sort()` and create an empty set `result` to hold unique triplets.
   - Loop with `for i in range(len(nums) - 2)` and fix `nums[i]` as the first number.
   - For each `i`, set `left = i + 1` and `right = len(nums) - 1`, then run `while left < right`:
     - Compute `total = nums[i] + nums[left] + nums[right]`.
     - If `total == 0`, add the tuple `(nums[i], nums[left], nums[right])` to `result`, then move both pointers (`left += 1`, `right -= 1`).
     - If `total < 0`, the sum is too small, so move `left += 1` to get a bigger number.
     - If `total > 0`, the sum is too big, so move `right -= 1` to get a smaller number.
   - At the end, convert each tuple in `result` back to a list and return them.

3. **Key insight:** After sorting, moving `left` right can only increase the sum and moving `right` left can only decrease it. So once `nums[i]` is fixed, the remaining "find two numbers" problem is solved in a single O(n) pass instead of a nested loop. Using a **set of tuples** removes duplicate triplets automatically (tuples are hashable, lists are not).

## Complexity

- **Time: O(n²).**
  - `nums.sort()` takes O(n log n).
  - The outer loop runs about `n - 2` times. For each `i`, the `while left < right` loop moves `left` up or `right` down on every iteration, so it runs at most `n - i - 2` times, which is O(n).
  - Together that is roughly `n + (n-1) + ... + 1`, i.e. O(n²). Adding a tuple to the set is O(1) on average.
  - O(n²) dominates O(n log n), so the total is **O(n²)**.
- **Space: O(k)**, where `k` is the number of unique triplets stored in the `result` set (and then copied into the returned list).
  - In the worst case `k` itself can grow up to O(n²), since an array can contain that many distinct zero-sum triplets.
  - `nums.sort()` also uses up to O(n) temporary space in Python (Timsort), and it modifies the input list in place.
  - If the returned output is not counted, the set is the only extra structure that depends on the answer, which is why this solution is not O(1) space.

## Mistakes & Learnings

For detailed notes, dry runs, edge cases, interview questions and a revision checklist, see [notes_README.md](./notes_README.md).