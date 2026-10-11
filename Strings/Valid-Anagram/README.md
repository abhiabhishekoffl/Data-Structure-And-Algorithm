\# 242. Valid Anagram



\*\*Difficulty:\*\* Easy

\*\*Link:\*\* \[LeetCode - Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

\*\*Pattern:\*\* Sorting (Sort and Compare)



\## Problem



Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.



An \*\*anagram\*\* is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.



\### Examples



| Input | Output | Explanation |

|-------|--------|-------------|

| `s = "anagram"`, `t = "nagaram"` | `true` | Both strings contain the same letters with the same counts. |

| `s = "rat"`, `t = "car"` | `false` | `s` has a `t` but `t` has a `c`, so the letters differ. |



\### Constraints



\- `1 <= s.length, t.length <= 5 \* 10^4`

\- `s` and `t` consist of lowercase English letters.



\*\*Follow-up:\*\* What if the inputs contain Unicode characters? How would you adapt your solution?



\## Approach



1\. \*\*Brute force:\*\* For every character in `s`, search for a matching character in `t` and remove it. If every character finds a match and nothing is left over, the strings are anagrams. Searching and removing inside a loop takes \*\*O(n²)\*\* time.



2\. \*\*Optimized (Sorting):\*\*

&#x20;  - Sort the characters of `s` with `s = sorted(s)`. This returns a \*\*list\*\* of characters in ascending order.

&#x20;  - Sort the characters of `t` the same way with `t = sorted(t)`.

&#x20;  - Compare the two sorted lists with `s == t`. If they are equal, return `True`. Otherwise, return `False`.



3\. \*\*Key insight:\*\* Two strings are anagrams exactly when they contain the same characters with the same counts, and only the order is different. Sorting removes the order difference, so after sorting, anagrams become \*\*identical\*\* lists, and a simple equality check is enough.



\## Complexity



Let `n = len(s)` and `m = len(t)`.



\- \*\*Time: O(n log n + m log m)\*\*, which is \*\*O(n log n)\*\* when the lengths are equal.

&#x20; - `sorted(s)` turns the string into a list of `n` characters in O(n), then sorts it in O(n log n).

&#x20; - `sorted(t)` does the same in O(m log m).

&#x20; - `s == t` compares two lists. If the lengths differ, Python returns `False` immediately in O(1). If the lengths are equal, it compares element by element in O(n).

&#x20; - The sorting dominates, so the total is \*\*O(n log n + m log m)\*\*. For anagrams `n == m`, so this is O(n log n).

\- \*\*Space: O(n + m).\*\*

&#x20; - Strings are immutable, so `sorted()` cannot sort in place. It builds a \*\*new list\*\* of characters for each string: O(n) for `s` and O(m) for `t`.

&#x20; - Python's sort (Timsort) can also use up to O(n) temporary space while sorting.

&#x20; - Reassigning `s` and `t` does not free the original strings, because the caller still holds them.

&#x20; - So the extra space is \*\*O(n + m)\*\*.



\## Mistakes \& Learnings



For detailed notes, dry runs, edge cases, interview questions and a revision checklist, see \[notes\_README.md](./notes\_README.md).

