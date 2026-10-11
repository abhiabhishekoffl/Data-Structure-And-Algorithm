# 📝 Valid Anagram: My Notes

The problem statement and approach live in `README.md`. This file is for my own revision, so that months later I can recall everything in five minutes.

---

## 🔑 Key Points

- **Topic:** Strings. **Pattern:** Sorting (sort both strings and compare).
- **Core idea:** Anagrams have exactly the same characters with the same counts. Sorting removes the order, so two anagrams become **identical** after sorting.
- `sorted(s)` returns a **list of characters**, not a string, because strings are immutable and cannot be sorted in place. Comparing two such lists with `==` works fine.
- **My solution:** O(n log n) time, O(n) space. It is short and easy to explain, but not the fastest option.
- **Faster option:** count the characters of each string instead of sorting. That gives O(n) time, and O(1) space for lowercase letters (a fixed array of 26 counters).
- Two strings of **different lengths** can never be anagrams. The list comparison catches this instantly, but the sorting is still done first, so checking `len(s) != len(t)` at the start saves work.
- `if s == t: return True else: return False` can be shortened to `return s == t`, because `==` already gives a boolean.
- **Follow-up (Unicode):** sorting works unchanged for any characters. The counting approach needs a hash map (for example `collections.Counter`) instead of a fixed array of 26.

---

## 🔍 Dry Run

**Example 1:** `s = "anagram"`, `t = "nagaram"`

| Step | Code | Result |
|:----:|------|--------|
| 1 | `s = sorted(s)` | `['a', 'a', 'a', 'g', 'm', 'n', 'r']` |
| 2 | `t = sorted(t)` | `['a', 'a', 'a', 'g', 'm', 'n', 'r']` |
| 3 | `s == t` | `True`, so return `True` ✅ |

**Example 2:** `s = "rat"`, `t = "car"`

| Step | Code | Result |
|:----:|------|--------|
| 1 | `s = sorted(s)` | `['a', 'r', 't']` |
| 2 | `t = sorted(t)` | `['a', 'c', 'r']` |
| 3 | `s == t` | `False` (the second elements differ: `'r'` vs `'c'`), so return `False` ✅ |

---

## ⏱️ Complexity (based on my solution)

```python
s = sorted(s)        # O(n) to build the list + O(n log n) to sort, creates a new list of n items
t = sorted(t)        # O(m) to build the list + O(m log m) to sort, creates a new list of m items
if s == t:           # O(1) if lengths differ, otherwise O(n) element-by-element comparison
    return True
else:
    return False
```

Let `n = len(s)` and `m = len(t)`.

### Time Complexity: O(n log n + m log m)

- **`sorted(s)`:** Python first copies the `n` characters into a list (O(n)), then sorts it with Timsort (O(n log n)).
- **`sorted(t)`:** the same for `m` characters, which is O(m log m).
- **`s == t`:** if the two lists have different lengths, Python returns `False` right away (O(1)). If the lengths are equal, it compares item by item (at most O(n)).
- **Total:** the sorting dominates, so the time is O(n log n + m log m). When the answer can be `True`, `n == m`, so this simplifies to **O(n log n)**.

### Space Complexity: O(n + m)

- `sorted()` returns a **new list**, so `s` becomes a list of `n` characters (O(n)) and `t` becomes a list of `m` characters (O(m)).
- Timsort can use up to O(n) extra temporary space while sorting.
- The original strings stay alive because the caller still references them, so reassigning `s` and `t` does not save memory.
- Total extra space: **O(n + m)**.

### Comparison

| Approach | Time | Space | Idea |
|----------|:----:|:-----:|------|
| Brute force (find and remove each character) | O(n²) | O(n) | Match characters one by one |
| Sorting (my solution) | O(n log n) | O(n) | Sort both and compare |
| Counting with an array of 26 | O(n) | O(1) | Count letters, then compare the counts |
| Counting with a hash map / `Counter` | O(n) | O(k) | Same, works for Unicode (k = distinct characters) |

---

## ⚠️ Edge Cases

- **Different lengths:** `"a"` and `"ab"` → `False`. They cannot be anagrams.
- **Same string:** `"abc"` and `"abc"` → `True`. A string is an anagram of itself.
- **Same letters, different counts:** `"aacc"` and `"ccac"` → `False`. Both have 4 letters, but `a` appears 2 times vs 1 time.
- **Single character:** `"a"` and `"a"` → `True`, and `"a"` and `"b"` → `False`.
- **Repeated letters:** `"anagram"` and `"nagaram"` → `True`. Counts matter, not only which letters exist.
- **Case:** `"Ab"` and `"ab"` → `False`, because uppercase and lowercase are different characters. The problem only uses lowercase letters.
- **Empty strings:** not allowed by the constraints, but `"" == ""` would return `True` in this code.

---

## 🎤 Interview Questions (related to this problem)

**1. What is the brute force approach, and how would you improve it?**
For each character in `s`, find and remove a matching character from `t`. That is O(n²). Sorting both strings and comparing them brings it to O(n log n), and counting characters brings it to O(n).

**2. Why does sorting work here?**
Anagrams contain the same characters with the same counts, and only the order differs. After sorting, the order is the same for both strings, so the sorted results are identical exactly when the strings are anagrams.

**3. What are the time and space complexity of your solution?**
Time is O(n log n) because of the sorting, and space is O(n) because `sorted()` creates new lists of characters.

**4. Why does `sorted(s)` return a list, and does it matter?**
Strings are immutable, so Python builds a new list of characters. It does not matter for comparison, because two lists of characters compare equal exactly when the sorted strings would. If a string is needed, use `"".join(sorted(s))`.

**5. Can you do better than O(n log n)?**
Yes, with character counting in O(n) time. Count the letters of `s` and `t` and compare the counts.

```python
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = [0] * 26
    for a, b in zip(s, t):
        count[ord(a) - ord("a")] += 1
        count[ord(b) - ord("a")] -= 1

    return all(c == 0 for c in count)
```

Time is O(n), and space is O(1) because the array always has 26 slots.

**6. Why is the counting solution O(1) space?**
The array has a fixed size of 26 for lowercase letters, no matter how long the strings are. This only holds for a fixed alphabet. For a larger character set, the space grows with the number of distinct characters.

**7. How would you handle Unicode characters? (the follow-up)**
Sorting already works for any characters. For the counting approach, replace the fixed array with a hash map, for example `Counter(s) == Counter(t)`. Space becomes O(k), where `k` is the number of distinct characters. For text with combined characters, normalize both strings first with `unicodedata.normalize`.

**8. Should you check the lengths first?**
Yes, it is a cheap early exit. If `len(s) != len(t)`, return `False` immediately and skip the sorting. It does not change the worst-case complexity, but it saves work.

**9. How can you simplify the final `if` / `else`?**
Return the comparison directly: `return s == t`. The expression already evaluates to `True` or `False`.

**10. What if uppercase letters, spaces or punctuation are allowed?**
Decide the rules first. For a case-insensitive check, use `s.lower()` and `t.lower()`. To ignore spaces or punctuation, filter them out before sorting or counting.

**11. How would you group a list of words into anagram groups?**
Use a dictionary where the key is the sorted word (or a tuple of 26 letter counts) and the value is the list of words with that key. All anagrams share the same key.

**12. Does your solution change the inputs?**
No. Strings are immutable, and `sorted()` builds new lists, so the original `s` and `t` objects stay as they were.

---

## ✅ Revision Checklist

- [ ] I can explain why sorting makes anagrams identical
- [ ] I can write the sorting solution without looking
- [ ] I can justify O(n log n) time and O(n) space, including why `sorted()` uses extra space
- [ ] I can write the O(n) counting solution with an array of 26
- [ ] I know how to adapt the solution for Unicode (hash map or `Counter`)
- [ ] I remember the edge cases (different lengths, same letters with different counts)