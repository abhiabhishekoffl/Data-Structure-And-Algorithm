\# 📝 Majority Element II: My Notes



The problem statement and approach live in `README.md`. This file is for my own revision, so that months later I can recall everything in five minutes.



\---



\## 🔑 Key Points



\- \*\*Pattern:\*\* Hash Map (Frequency Count). Count how many times each number appears, then keep the numbers whose count is greater than `n // 3`.

\- \*\*At most 2 answers.\*\* If three different numbers each appeared more than `n / 3` times, together they would be more than `n` elements, which is impossible. This fact is the heart of the problem, and it is also what makes the O(1) space follow-up possible.

\- The condition is \*\*strictly greater than\*\*: `value > n // 3`. A number that appears exactly `n / 3` times does \*\*not\*\* count (for example `\[1,1,2,2,3,3]` returns `\[]`).

\- Using `n // 3` (floor) is the same as using the real `n / 3`, because counts are integers. For `n = 7`, `7 // 3 = 2`, and "count > 2" is the same as "count > 2.33".

\- For tiny arrays the threshold is `0`, so every distinct element qualifies: `\[1]` → `\[1]` and `\[1, 2]` → `\[1, 2]`.

\- \*\*My solution:\*\* O(n) time, O(n) space. It does not meet the "O(1) space" follow-up. For that, use \*\*Boyer-Moore Voting with two candidates\*\* (see the interview questions below).

\- Always compute `n // 3` from the \*\*original length\*\* of the array, not from the number of distinct elements.



\---



\## 🔍 Dry Run



`nums = \[3, 2, 3]`, so `n = 3` and `n // 3 = 1`



\*\*Step 1: build the frequency map\*\*



| num | Already in hashmap? | hashmap after this step |

|:---:|:-------------------:|-------------------------|

| 3 | No | `{3: 1}` |

| 2 | No | `{3: 1, 2: 1}` |

| 3 | Yes | `{3: 2, 2: 1}` |



\*\*Step 2: filter with `value > n // 3`\*\*



| key | value | `value > 1`? | result |

|:---:|:-----:|:------------:|--------|

| 3 | 2 | Yes | `\[3]` |

| 2 | 1 | No | `\[3]` |



Final result: `\[3]`.



A second example with two answers: `nums = \[1, 1, 1, 3, 3, 2, 2, 2]`, so `n = 8` and `n // 3 = 2`



| key | value | `value > 2`? | result |

|:---:|:-----:|:------------:|--------|

| 1 | 3 | Yes | `\[1]` |

| 3 | 2 | No | `\[1]` |

| 2 | 3 | Yes | `\[1, 2]` |



Final result: `\[1, 2]`.



\---



\## ⏱️ Complexity (based on my solution)



```python

n = len(nums)                         # O(1)

hashmap = {}



for num in nums:                      # runs n times

&#x20;   if num in hashmap:                # O(1) average lookup

&#x20;       hashmap\[num] += 1             # O(1) average read + write

&#x20;   else:

&#x20;       hashmap\[num] = 1              # O(1) average insert



result = \[]



for key, value in hashmap.items():    # runs once per distinct number (at most n times)

&#x20;   if value > n // 3:                # O(1) comparison

&#x20;       result.append(key)            # O(1) append (result never exceeds 2 elements)



return result

```



\### Time Complexity: O(n)



\- \*\*First loop:\*\* exactly `n` iterations. Each one does a dictionary lookup and a write, both O(1) on average, so this part is O(n).

\- \*\*Second loop:\*\* one iteration per distinct number. There can be at most `n` of them, and each iteration is O(1), so this part is at most O(n).

\- \*\*Total:\*\* O(n) + O(n) = \*\*O(n)\*\*.

\- There is no early return, so the best case and the worst case are both O(n). The only thing that changes is the size of `hashmap`.

\- \*Technical note:\* heavy hash collisions could make a single dictionary operation O(n) in theory. In practice and in interviews, dictionary operations are treated as O(1) average.



\### Space Complexity: O(n)



\- `hashmap` holds one entry per distinct number.

&#x20; - \*\*Worst case:\*\* all `n` numbers are different, so it holds `n` entries → O(n).

&#x20; - \*\*Best case:\*\* all numbers are the same, so it holds 1 entry → O(1).

&#x20; - The worst case decides the answer: \*\*O(n)\*\*.

\- `result` holds at most 2 elements → O(1).

\- `n`, `num`, `key` and `value` are single values → O(1).

\- There is no recursion, so there is no extra call stack space.



\### Comparison



| Approach | Time | Space | Idea |

|----------|:----:|:-----:|------|

| Brute force (count each element by scanning) | O(n²) | O(1) | Scan the array for every element |

| Sorting + scan runs | O(n log n) | O(1) to O(n), depends on the sort | Equal numbers become neighbours, so count each run |

| Hash map (my solution) | O(n) | O(n) | Count frequencies, then filter |

| Boyer-Moore Voting (two candidates) | O(n) | O(1) | Keep 2 candidates and cancel out the rest, then verify |



So the hash map buys speed with memory, and Boyer-Moore gets both.



\---



\## ⚠️ Edge Cases



\- \*\*Single element:\*\* `\[1]` → `\[1]`, because `n // 3 = 0` and `1 > 0`.

\- \*\*Two elements:\*\* `\[1, 2]` → `\[1, 2]`, because `n // 3 = 0`, so both qualify.

\- \*\*All elements equal:\*\* `\[2, 2, 2]` → `\[2]`.

\- \*\*No majority:\*\* `\[1, 2, 3, 4, 5, 6]` → `\[]`, because `n // 3 = 2` and every count is `1`.

\- \*\*Exactly `n / 3` times:\*\* `\[1, 1, 2, 2, 3, 3]` → `\[]`, because each count is `2` and `2 > 2` is false.

\- \*\*Negative numbers and zero:\*\* work the same, because the dictionary accepts any integer as a key.

\- \*\*Order of the output:\*\* any order is accepted. This solution returns numbers in the order they first appeared in `nums`.

\- \*\*Empty list:\*\* not allowed by the constraints, but the code would return `\[]` safely.



\---



\## 🎤 Interview Questions (related to this problem)



\*\*1. What is the brute force approach, and how would you improve it?\*\*

For each element, scan the whole array to count it. That is O(n²) time, and it also needs care to avoid returning the same number twice. Counting all frequencies once with a hash map brings it down to O(n) time.



\*\*2. Why can there be at most two answers?\*\*

Each answer must appear more than `n / 3` times. Three such numbers would take up more than `n` positions in total, which is impossible. So the answer has 0, 1 or 2 elements.



\*\*3. Why `> n // 3` and not `>= n // 3`?\*\*

The problem says "more than". An element that appears exactly `n / 3` times does not count. For example `\[1,1,2,2,3,3]` has `n // 3 = 2` and every count is `2`, so the correct answer is `\[]`.



\*\*4. Is using `n // 3` correct when `n` is not divisible by 3?\*\*

Yes. Counts are integers, so "count > ⌊n/3⌋" is exactly the same as "count > n/3". For `n = 7`, `7 // 3 = 2` and a count of `3` passes both checks, while a count of `2` fails both.



\*\*5. What are the time and space complexity of your solution?\*\*

Time O(n): one pass to count and one pass over at most `n` distinct keys. Space O(n): the dictionary can hold up to `n` distinct numbers in the worst case.



\*\*6. Can you solve it in O(1) space? (the follow-up)\*\*

Yes, with Boyer-Moore Voting using two candidates. Since there are at most 2 answers, keep two candidate numbers and two counters.



```python

def majorityElement(nums):

&#x20;   cand1 = cand2 = None

&#x20;   cnt1 = cnt2 = 0



&#x20;   for num in nums:

&#x20;       if num == cand1:

&#x20;           cnt1 += 1

&#x20;       elif num == cand2:

&#x20;           cnt2 += 1

&#x20;       elif cnt1 == 0:

&#x20;           cand1, cnt1 = num, 1

&#x20;       elif cnt2 == 0:

&#x20;           cand2, cnt2 = num, 1

&#x20;       else:

&#x20;           cnt1 -= 1

&#x20;           cnt2 -= 1



&#x20;   result = \[]

&#x20;   for cand in (cand1, cand2):

&#x20;       if cand is not None and nums.count(cand) > len(nums) // 3:

&#x20;           result.append(cand)

&#x20;   return result

```



Time is O(n) and space is O(1).



\*\*7. Why does Boyer-Moore need a second pass?\*\*

The first pass only finds the two numbers that could be the answers, not numbers that are guaranteed to be answers. There may be no valid majority at all (for example `\[1,2,3,4,5,6]`), so every candidate must be verified by counting its real frequency.



\*\*8. Why does decrementing both counters work?\*\*

When a number matches neither candidate and both counters are non-zero, it cancels one vote from each candidate. That removes three different numbers from consideration at once. A number that appears more than `n / 3` times can never be fully cancelled out, because the cancellations can only remove at most `n / 3` groups of three.



\*\*9. Can you solve it by sorting?\*\*

Yes. Sort the array, then walk through it counting the length of each run of equal numbers, and keep the numbers whose run is longer than `n // 3`. This is O(n log n) time. It avoids the hash map, but it is slower and it modifies the input if sorted in place.



\*\*10. Can you make the counting code shorter?\*\*

Yes. Use `collections.Counter(nums)` to build the frequency map in one line, then filter it with a list comprehension. It is the same O(n) time and O(n) space, just less code.



\*\*11. How would you generalize this to "more than n / k" times?\*\*

At most `k - 1` numbers can appear more than `n / k` times. The hash map solution works unchanged with the new threshold. The O(1)-style version keeps `k - 1` candidates, giving O(n·k) time and O(k) space. For `k = 2` this is the classic Majority Element problem with a single candidate.



\*\*12. Does your solution change the input?\*\*

No. It only reads `nums`, and uses extra memory for `hashmap` and `result`.



\---



\## ✅ Revision Checklist



\- \[ ] I can explain why there are at most 2 answers

\- \[ ] I can write the hash map solution without looking

\- \[ ] I know why the condition is strictly `>` and not `>=`

\- \[ ] I can justify O(n) time and O(n) space for my solution

\- \[ ] I can explain Boyer-Moore Voting with two candidates and why it needs a second pass

\- \[ ] I remember the edge cases (`\[1]`, `\[1,2]`, exactly `n / 3`)

