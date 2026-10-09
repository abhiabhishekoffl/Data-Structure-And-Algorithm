\# 229. Majority Element II



\*\*Difficulty:\*\* Medium

\*\*Link:\*\* \[LeetCode - Majority Element II](https://leetcode.com/problems/majority-element-ii/description/)

\*\*Pattern:\*\* Hash Map (Frequency Count)



\## Problem



Given an integer array `nums` of size `n`, return \*\*all the elements that appear more than `⌊n / 3⌋` times\*\*.



The answer can be returned in any order.



\### Examples



| Input | Output | Explanation |

|-------|--------|-------------|

| `nums = \[3,2,3]` | `\[3]` | `n = 3`, so `⌊n/3⌋ = 1`. Only `3` appears more than once. |

| `nums = \[1]` | `\[1]` | `n = 1`, so `⌊n/3⌋ = 0`. `1` appears more than 0 times. |

| `nums = \[1,2]` | `\[1,2]` | `n = 2`, so `⌊n/3⌋ = 0`. Both numbers appear more than 0 times. |



\### Constraints



\- `1 <= nums.length <= 5 \* 10^4`

\- `-10^9 <= nums\[i] <= 10^9`



\*\*Follow-up:\*\* Could you solve the problem in linear time and in `O(1)` space?



\## Approach



1\. \*\*Brute force:\*\* For every element, count how many times it appears by scanning the whole array, and keep it if the count is more than `n // 3`. This takes \*\*O(n²)\*\* time, and you also have to avoid adding the same element twice.



2\. \*\*Optimized (Hash Map):\*\*

&#x20;  - Store `n = len(nums)` and create an empty dictionary `hashmap` that maps each number to its frequency.

&#x20;  - Loop through `nums` once. For each `num`, if it is already in `hashmap`, do `hashmap\[num] += 1`. Otherwise, set `hashmap\[num] = 1`.

&#x20;  - Create an empty list `result`.

&#x20;  - Loop through `hashmap.items()`. For each `key, value` pair, if `value > n // 3`, append `key` to `result`.

&#x20;  - Return `result`.



3\. \*\*Key insight:\*\* At most \*\*two\*\* numbers can appear more than `n / 3` times. If three different numbers each appeared more than `n / 3` times, their counts together would be more than `n`, which is impossible. So the answer never has more than 2 elements, and counting frequencies with a hash map is enough to find them.



\## Complexity



\- \*\*Time: O(n).\*\*

&#x20; - The first loop runs `n` times. Each iteration does one `in` check, and one dictionary read/write. These are O(1) on average, so the loop costs O(n).

&#x20; - The second loop goes through `hashmap.items()`, which has at most `n` distinct keys (when every number is different). Each iteration is an O(1) comparison and an O(1) append, so it costs at most O(n).

&#x20; - Total = O(n) + O(n) = \*\*O(n)\*\*. There is no early exit, so the best case and the worst case are both O(n).

\- \*\*Space: O(n).\*\*

&#x20; - `hashmap` stores one entry per distinct number. In the worst case all `n` numbers are different, so it holds `n` entries.

&#x20; - In the best case (all numbers equal) it holds just 1 entry, but the worst case decides the complexity.

&#x20; - `result` holds at most 2 elements, so it is O(1). The variable `n` is O(1).

&#x20; - So this solution does \*\*not\*\* meet the O(1) space follow-up. That needs the Boyer-Moore Voting idea, explained in `notes\_README.md`.



\## Mistakes \& Learnings



For detailed notes, dry runs, edge cases, interview questions and a revision checklist, see \[notes\_README.md](./notes\_README.md).

