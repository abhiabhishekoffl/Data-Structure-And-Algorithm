\# 1. Two Sum



\*\*Difficulty:\*\* Easy

\*\*Link:\*\* \[LeetCode - Two Sum](https://leetcode.com/problems/two-sum/description/)

\*\*Pattern:\*\* Hash Map (Complement Lookup)



\## Problem



Ek integer array `nums` aur ek integer `target` diya hai. Aise \*\*do alag indices\*\* return karo jinke elements ka sum `target` ke barabar ho.



\- Har input me \*\*exactly ek valid answer\*\* hota hai.

\- Same element ko do baar use nahi kar sakte.

\- Answer kisi bhi order me return kar sakte ho.



\### Examples



| Input | Output | Explanation |

|-------|--------|-------------|

| `nums = \[2,7,11,15], target = 9` | `\[0,1]` | `nums\[0] + nums\[1] = 2 + 7 = 9` |

| `nums = \[3,2,4], target = 6` | `\[1,2]` | `nums\[1] + nums\[2] = 2 + 4 = 6` |

| `nums = \[3,3], target = 6` | `\[0,1]` | `nums\[0] + nums\[1] = 3 + 3 = 6` |



\### Constraints



\- `2 <= nums.length <= 10^4`

\- `-10^9 <= nums\[i] <= 10^9`

\- `-10^9 <= target <= 10^9`

\- Exactly one valid answer exists.



\*\*Follow-up:\*\* Kya O(n²) se better algorithm de sakte ho?



\## Approach



1\. \*\*Brute force:\*\* Har pair `(i, j)` check karo ki `nums\[i] + nums\[j] == target` hai ya nahi. Ye simple hai, lekin do nested loops ki wajah se \*\*O(n²)\*\* time lagta hai, jo badi input pe slow hai.



2\. \*\*Optimized (Hash Map):\*\* Array ko ek hi baar traverse karo. Har element `nums\[i]` ke liye uska \*\*complement\*\* `target - nums\[i]` nikalo.

&#x20;  - Agar complement pehle se `seen\_elements` dictionary me hai, to answer mil gaya: `\[seen\_elements\[complement], i]`.

&#x20;  - Warna current element ko `seen\_elements\[nums\[i]] = i` ke saath store kar do.



3\. \*\*Key insight:\*\* "Kya mujhe koi pichla number mila jo mujhe target tak pahunchaye?" is sawal ka jawab \*\*O(1)\*\* me hash map se milta hai. Isliye har element ke liye pura array dobara scan nahi karna padta.



\## Complexity



\- \*\*Time:\*\* O(n), array ek hi baar traverse hota hai aur dictionary lookup/insert O(1) average hai.

\- \*\*Space:\*\* O(n), worst case me saare elements dictionary me store ho jaate hain.



\## Mistakes \& Learnings



Detailed notes, dry run, edge cases aur revision checklist ke liye dekho: \[notes\_README.md](./notes\_README.md)

