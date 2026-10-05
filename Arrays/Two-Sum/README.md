# 1. Two Sum

**Difficulty:** Easy
**Link:** [LeetCode - Two Sum](https://leetcode.com/problems/two-sum/description/)
**Pattern:** Hash Map (Complement Lookup)

## Problem

Given an integer array `nums` and an integer `target`, return the indices of the **two distinct elements** whose sum equals `target`.

- Each input has **exactly one valid answer**.
- The same element cannot be used twice.
- The answer can be returned in any order.

### Examples

| Input | Output | Explanation |
|-------|--------|-------------|
| `nums = [2,7,11,15], target = 9` | `[0,1]` | `nums[0] + nums[1] = 2 + 7 = 9` |
| `nums = [3,2,4], target = 6` | `[1,2]` | `nums[1] + nums[2] = 2 + 4 = 6` |
| `nums = [3,3], target = 6` | `[0,1]` | `nums[0] + nums[1] = 3 + 3 = 6` |

### Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Exactly one valid answer exists.

**Follow-up:** Can you come up with an algorithm that is better than O(n²)?

## Approach

1. **Brute force:** Check every pair `(i, j)` and test whether `nums[i] + nums[j] == target`. It is simple, but the two nested loops make it **O(n²)**, which is slow for large inputs.

2. **Optimized (Hash Map):** Traverse the array once. For each element `nums[i]`, compute its **complement**, `target - nums[i]`.
   - If the complement is already in `seen_elements`, we have the answer: `[seen_elements[complement], i]`.
   - Otherwise, store the current element with `seen_elements[nums[i]] = i`.

3. **Key insight:** The question "have I already seen a number that completes the target?" can be answered in **O(1)** with a hash map, so we never need to rescan the array for each element.

## Complexity

- **Time:** O(n). The array is traversed once, and each dictionary lookup/insert is O(1) on average.
- **Space:** O(n). In the worst case, almost all elements are stored in the dictionary.

## Mistakes & Learnings

For detailed notes, dry runs, edge cases, interview questions and a revision checklist, see [notes_README.md](./notes_README.md).