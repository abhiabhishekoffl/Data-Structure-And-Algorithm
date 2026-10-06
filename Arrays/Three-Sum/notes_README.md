\# 📝 Two Sum: Notes



Ye file revision ke liye hai. Problem ka statement aur approach `README.md` me hai, yahan sirf mera personal learning aur quick recall hai.



\## 🧠 Pattern Recognition



Jab bhi problem me aisa kuch dikhe:



\- "Do elements dhundho jinka sum/difference/product target ho"

\- "Pehle dekhe hue elements ko yaad rakhna hai"



to sochna chahiye: \*\*Hash Map me complement store karo.\*\*



\## 🔍 Dry Run



`nums = \[2, 7, 11, 15]`, `target = 9`



| i | nums\[i] | complement (target - nums\[i]) | seen\_elements (check se pehle) | Action |

|:-:|:-------:|:-----------------------------:|:------------------------------:|--------|

| 0 | 2 | 7 | `{}` | 7 nahi mila, `{2: 0}` store kiya |

| 1 | 7 | 2 | `{2: 0}` | 2 mil gaya, return `\[0, 1]` ✅ |



\## ⚠️ Edge Cases



\- \*\*Duplicate values:\*\* `\[3, 3], target = 6`. Pehle check hota hai, phir store, isliye dusra `3` pehle wale `3` ko match kar leta hai.

\- \*\*Negative numbers:\*\* `\[-1, -2, -3, -4, -5], target = -8`. Approach waise hi kaam karti hai.

\- \*\*Zero:\*\* `\[0, 4, 3, 0], target = 0`. Complement `0` hai, aur do alag indices milte hain.

\- \*\*Same element dobara use nahi hota:\*\* kyunki current element ko dictionary me \*\*check ke baad\*\* daalte hain.



\## 💡 Learnings



\- Dictionary me \*\*value → index\*\* store karna hai, kyunki answer me indices chahiye, values nahi.

\- \*\*Check pehle, store baad me.\*\* Agar pehle store karenge to `target = 2 \* nums\[i]` jaise case me element khud se match ho jayega.

\- Sorting + two pointers bhi ek approach hai, lekin sorting se original indices badal jaate hain, isliye is problem ke liye hash map zyada seedha hai.



\## ❌ Mistakes (apne words me bharna)



\- \[ ] Pehli baar me maine kya galti ki:

\- \[ ] Next time kya yaad rakhna hai:



\## 🔗 Related Problems



\- 167. Two Sum II - Input Array Is Sorted (two pointers)

\- 15. 3Sum

\- 653. Two Sum IV - Input is a BST

\- 560. Subarray Sum Equals K (prefix sum + hash map)



\## ✅ Revision Checklist



\- \[ ] Brute force bata sakta hoon (O(n²))

\- \[ ] Hash map approach bina dekhe likh sakta hoon

\- \[ ] Time aur space complexity explain kar sakta hoon

\- \[ ] Duplicate wala edge case samajh aaya

