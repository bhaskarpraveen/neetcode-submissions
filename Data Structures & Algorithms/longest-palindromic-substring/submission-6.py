class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        count = 0
        st = ""

        for i in range(n):
            # Check for odd-length palindrome
            f, j = i, i  
            while f >= 0 and j < n and s[f] == s[j]:
                if j - f + 1 > count:  # Update only if it's strictly longer
                    count = j - f + 1
                    st = s[f:j+1]
                f -= 1
                j += 1

            # Check for even-length palindrome
            f, j = i, i + 1  
            while f >= 0 and j < n and s[f] == s[j]:
                if j - f + 1 > count:
                    count = j - f + 1
                    st = s[f:j+1]
                f -= 1
                j += 1

        return st
