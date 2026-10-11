class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
    print(sol.isAnagram("a", "ab"))             # False
    print(sol.isAnagram("aacc", "ccac"))        # False
    print(sol.isAnagram("listen", "silent"))    # True