# 📝 3Sum: My Notes

The problem statement and approach live in `README.md`. This file is for my own revision, so that months later I can recall everything in five minutes.

---

## 🔑 Key Points

- **Pattern:** Sorting + Two Pointers. 3Sum is Two Sum with one extra fixed number: *"fix `nums[i]`, then find two numbers that add up to `-nums[i]`."*
- **Sorting is what makes the pointers work.** After sorting, `left` moves toward bigger values and `right` moves toward smaller values, so I always know which pointer to move.
- **Pointer rules (memorize these):**
  - `total < 0` → sum too small → `left += 1`
  - `total > 0` → sum too big → `right -= 1`
  - `total == 0` → store the triplet → move **both** pointers
- The same triplet can be found more than once (for example from two different `-1` values), so the answer needs de-duplication. My solution does this with a `set` of **tuples**.
- Use a **tuple, not a list**, inside a set, because lists are mutable and not hashable.
- The answer contains **values**, not indices. That is why sorting is allowed here (unlike Two Sum, where indices are required).
- `range(len(nums) - 2)` is enough for `i`, because `left` and `right` need two more elements after it.

---

## 🔍 Dry Run

`nums = [-1, 0, 1, 2, -1, -4]` → after `nums.sort()` → `[-4, -1, -1, 0, 1, 2]`

| i | nums[i] | left | right | total | What happens |
|:-:|:-------:|:----:|:-----:|:-----:|--------------|
| 0 | -4 | 1 | 5 | -3 | `< 0`, `left += 1` |
| 0 | -4 | 2 | 5 | -3 | `< 0`, `left += 1` |
| 0 | -4 | 3 | 5 | -2 | `< 0`, `left += 1` |
| 0 | -4 | 4 | 5 | -1 | `< 0`, `left += 1`, then `left == right`, loop ends |
| 1 | -1 | 2 | 5 | 0 | Add `(-1, -1, 2)`, move both pointers |
| 1 | -1 | 3 | 4 | 0 | Add `(-1, 0, 1)`, move both pointers, loop ends |
| 2 | -1 | 3 | 5 | 1 | `> 0`, `right -= 1` |
| 2 | -1 | 3 | 4 | 0 | Triplet `(-1, 0, 1)` is found **again**, the set ignores it |
| 3 | 0 | 4 | 5 | 3 | `> 0`, `right -= 1`, then `left == right`, loop ends |

Final result: `[[-1, -1, 2], [-1, 0, 1]]` (order may vary, because a set is unordered).

The `i = 2` row is why the set is needed: the second `-1` finds the same triplet again.

---

## ⏱️ Complexity (based on my solution)

```python
nums.sort()                                      # O(n log n)
result = set()

for i in range(len(nums) - 2):                   # about n iterations
    left = i + 1
    right = len(nums) - 1

    while left < right:                          # up to n - i - 2 iterations
        total = nums[i] + nums[left] + nums[right]

        if total == 0:
            result.add((nums[i], nums[left], nums[right]))   # O(1) average
            left += 1
            right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1

return [list(triplet) for triplet in result]     # O(k) for k unique triplets
```

### Time Complexity: O(n²)

- **Sorting:** O(n log n).
- **Outer loop:** runs about `n - 2` times.
- **Inner `while`:** in every iteration, `left` increases or `right` decreases (or both), and the loop stops when they meet. So for one `i` it runs at most `n - i - 2` times, which is O(n). It never restarts, so there is no hidden third loop.
- **Total work:** roughly `n + (n-1) + (n-2) + ... + 1`, which is about `n²/2`, so **O(n²)**.
- **Set insert:** hashing a 3-element tuple and inserting it is O(1) on average, so it does not change the total.
- **Final conversion:** O(k) for `k` unique triplets, and `k` is at most O(n²), so it is also covered.
- Overall: O(n log n) + O(n²) = **O(n²)**.

### Space Complexity: O(k) (up to O(n²) in the worst case)

- The `result` set stores every unique triplet found, so it takes O(k) space, where `k` is the number of unique triplets. The returned list is another O(k) copy.
- In the worst case `k` itself can reach O(n²), because an array can have that many distinct zero-sum triplets.
- `nums.sort()` sorts in place (it changes the input list) but Python's Timsort can use up to O(n) temporary space.
- Other variables (`i`, `left`, `right`, `total`) are O(1).
- **Takeaway:** if the output is not counted, a solution that skips duplicates directly (instead of using a set) needs only O(1) to O(n) auxiliary space depending on the sort. My set-based version trades some extra memory for simpler duplicate handling.

### Comparison

| Approach | Time | Extra space | Idea |
|----------|:----:|:-----------:|------|
| Brute force (three nested loops) | O(n³) | O(k) | Check every triplet |
| Sort + two pointers + set (my solution) | O(n²) | O(k) | Fix one, two pointers for the rest, set removes duplicates |
| Sort + two pointers + skip duplicates | O(n²) | O(1) (excluding output) | Same, but skip equal neighbours instead of using a set |

---

## ⚠️ Edge Cases

- **Fewer than 3 elements:** `[1, 2]` → `[]` (handled by the first `if`).
- **No valid triplet:** `[1, 2, 3]` → `[]`, because all numbers are positive and no sum can be 0.
- **All zeros:** `[0, 0, 0, 0]` → `[[0, 0, 0]]`. Many pointer positions give the same triplet, and the set keeps just one.
- **Duplicates:** `[-1, 0, 1, 2, -1, -4]`. The same triplet is found more than once, and the set removes the repeats.
- **Mixed signs:** `[-2, 0, 2]` → `[[-2, 0, 2]]`.
- **Input is modified:** `nums.sort()` changes the original list. If the original order matters, sort a copy.

---

## 🎤 Interview Questions (related to this problem)

**1. What is the brute force approach, and how would you improve it?**
Three nested loops checking every triplet is O(n³). Sorting the array and fixing one number while using two pointers for the other two brings it to O(n²).

**2. Why do you sort the array first?**
Sorting makes pointer movement predictable. If the sum is too small, moving `left` right increases it. If it is too big, moving `right` left decreases it. Without sorting, I couldn't decide which pointer to move.

**3. Why is the time complexity O(n²) and not O(n³)?**
The two-pointer `while` loop makes a single pass over the rest of the array (O(n)) for each fixed `i`. It is not a nested loop, so the total is O(n) × O(n) = O(n²).

**4. Why do you use a set, and why store tuples instead of lists?**
The same triplet can be found more than once, and the problem forbids duplicates. A set keeps each triplet once. Tuples are hashable and lists are not, so triplets must be tuples while inside the set.

**5. What is the space complexity of your solution?**
O(k), where `k` is the number of unique triplets stored in the set, which can be up to O(n²) in the worst case. The sort adds up to O(n) temporary space.

**6. How can you avoid the extra set?**
Skip duplicates directly. After sorting, if `i > 0 and nums[i] == nums[i - 1]`, skip that `i`. After finding a triplet, move `left` past equal values and `right` past equal values. Then every triplet is generated only once and no set is needed.

**7. What if the sum is zero, why move both pointers?**
With the same `i` and the same `right`, only a `left` holding an equal value could sum to zero again, and that would just be the same triplet. The same is true if only `right` moved while `left` stayed. So any new triplet needs both values to change, which makes moving both pointers safe.

**8. Can you solve it with a hash map like Two Sum?**
Yes. Fix `nums[i]` and run a Two Sum with a hash map on the remaining elements, which is also O(n²). But duplicates are harder to handle, and sorting + two pointers uses less extra memory.

**9. Can you stop early to make it faster?**
Yes. Because the array is sorted, once `nums[i] > 0`, all three numbers are positive and the sum can never be 0, so you can `break`. This does not change the worst-case complexity.

**10. What if the question asked for indices instead of values?**
Sorting would destroy the original indices. You would need to store `(value, original_index)` pairs before sorting, or use a hash-map-based approach.

**11. What changes for 4Sum?**
Fix two numbers with two nested loops and use two pointers for the other two. Time becomes O(n³). In general, k-Sum is O(n^(k-1)) with this technique.

**12. Does your solution change the input?**
Yes, `nums.sort()` sorts the list in place. If that is not allowed, sort a copy (`sorted(nums)`), which costs O(n) extra space.

---

## ✅ Revision Checklist

- [ ] I can explain why brute force is O(n³)
- [ ] I can write the sort + two pointers solution without looking
- [ ] I remember the three pointer rules (`< 0`, `> 0`, `== 0`)
- [ ] I can explain why the set needs tuples, not lists
- [ ] I can justify O(n²) time and the space cost of the set
- [ ] I know how to skip duplicates instead of using a set