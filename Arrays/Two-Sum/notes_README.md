# 📝 Two Sum: My Notes

The problem statement and approach live in `README.md`. This file is for my own revision, so that months later I can recall everything in five minutes.

---

## 🔑 Key Points

- **Pattern:** Hash Map + Complement. For every number, ask: *"Have I already seen the number I need (`target - nums[i]`)?"*
- The dictionary stores **value → index**, because the answer needs indices, not values.
- **Check first, then store.** This order is what stops an element from matching itself (for example, `3` in `[3, 2, 4]` with target `6`).
- The array is traversed **only once**, which brings the brute force O(n²) down to O(n).
- The problem guarantees exactly one answer, so we return the moment we find it.
- This idea shows up everywhere: *"remember what you have already seen"* becomes an O(1) lookup with a hash map.

---

## 🔍 Dry Run

`nums = [2, 7, 11, 15]`, `target = 9`

| i | nums[i] | Needed (target - nums[i]) | seen_elements (before check) | What happens |
|:-:|:-------:|:-------------------------:|:----------------------------:|--------------|
| 0 | 2 | 7 | `{}` | 7 not found, store `{2: 0}` |
| 1 | 7 | 2 | `{2: 0}` | 2 found, return `[0, 1]` ✅ |

Duplicate case: `nums = [3, 3]`, `target = 6`

| i | nums[i] | Needed | seen_elements (before check) | What happens |
|:-:|:-------:|:------:|:----------------------------:|--------------|
| 0 | 3 | 3 | `{}` | not found, store `{3: 0}` |
| 1 | 3 | 3 | `{3: 0}` | found, return `[0, 1]` ✅ |

---

## ⏱️ Complexity (based on my solution)

```python
seen_elements = {}
for i in range(len(nums)):                      # runs at most n times
    if target - nums[i] in seen_elements:       # subtraction O(1) + dict lookup O(1) average
        return [seen_elements[target - nums[i]], i]   # dict read O(1)
    seen_elements[nums[i]] = i                  # dict insert O(1) average
```

### Time Complexity: O(n)

- The loop runs at most **n** iterations (n = `len(nums)`).
- Everything inside an iteration is constant time: one subtraction, one dictionary lookup (`in`), one dictionary read, and one dictionary insert. Python dict operations are **O(1) on average**.
- Total = n × O(1) = **O(n)**.
- **Best case:** the answer is found among the first two elements (at i = 1), so the work is O(1).
- **Worst case:** the answer is found at the very end (at i = n-1), so the whole array is traversed, which is O(n).
- *Technical note:* with extreme hash collisions, a single dict operation could degrade to O(n), but in practice and in interviews dict operations are treated as O(1) average.

### Space Complexity: O(n)

- `seen_elements` grows as we store elements.
- In the worst case the answer is found at the last index, by which time the dictionary holds **n - 1** entries, so space is **O(n)**.
- The loop variable `i` and everything else take constant space. In Python 3, `range()` is a lazy object and does not build a full list.
- There is no recursion, so there is no extra call stack space either.

### Comparison with brute force

| Approach | Time | Space | Idea |
|----------|:----:|:-----:|------|
| Brute force (two nested loops) | O(n²) | O(1) | Check every pair |
| Hash map (my solution) | O(n) | O(n) | Look up the complement in a dictionary |

So I traded **space for time**: a little extra memory buys a big speedup.

---

## ⚠️ Edge Cases

- **Duplicate values:** `[3, 3]`, target `6`. The check happens first, so the second `3` matches the first one.
- **Negative numbers:** `[-1, -2, -3, -4, -5]`, target `-8`. The logic works unchanged.
- **Zero:** `[0, 4, 3, 0]`, target `0`. The two zeros at indices `[0, 3]` are found.
- **Same element twice:** `[3, 2, 4]`, target `6`. `3 + 3` is not counted, and the answer is `[1, 2]`.

---

## 🎤 Interview Questions (related to this problem)

**1. What is the brute force approach, and how would you improve it?**
Use two nested loops to check every pair, which takes O(n²) time. To improve it, store complements in a hash map, giving O(n) time and O(n) space.

**2. What do you store as key and value in the hash map, and why?**
Key = the number, value = its index. We must return indices, so the index goes in the value, and the lookup is done by number.

**3. Do you check first or store first? What happens if you swap the order?**
Check first, then store. If you store first, then when `target = 2 * nums[i]` (for example `[3, 2, 4]` with target `6`), an element would match itself and give a wrong answer.

**4. How do you handle duplicates?**
If two equal values form the answer, the first one is already in the dictionary when the second one arrives, so it matches immediately. Overwriting a value in the dictionary is never a problem before the answer is found.

**5. What if there is no valid pair?**
This problem guarantees exactly one answer. In real code, return `[]` or `None` after the loop, and state that assumption to the interviewer.

**6. What if there can be multiple valid pairs and you need all of them?**
Don't return inside the loop; collect pairs in a list instead. If values repeat, store a list of indices per value in the dictionary.

**7. What if the array is already sorted?**
Use two pointers: `left = 0`, `right = n - 1`. If the sum is too small, move `left` forward; if too large, move `right` back. Time O(n), space **O(1)**.

**8. What if you only need values, not indices?**
Sort the array and use two pointers. Sorting costs O(n log n) with O(1) extra space (if sorted in place). If you need indices, you can't simply sort, because original positions get lost.

**9. When would you pick the hash map over two pointers?**
Hash map for an unsorted array when indices are required. Two pointers for a sorted array or when memory is tight.

**10. What if memory is very limited?**
Avoid O(n) space by using sort + two pointers (for values), or fall back to brute force with O(1) space. It is a time vs. space trade-off.

**11. What is the worst-case complexity of a hash map?**
With a huge number of collisions a single operation can take O(n), making the total O(n²). On average each operation is O(1), and that is what is assumed in practice.

**12. What if you need three numbers that sum to the target?**
Sort the array, fix one number, and use two pointers for the other two. Total time O(n²).

---

## ✅ Revision Checklist

- [ ] I can explain the brute force approach (O(n²))
- [ ] I can write the hash map solution without looking
- [ ] I can justify the time and space complexity
- [ ] I know why we "check first, then store"
- [ ] I remember the sorted-array two-pointer variant