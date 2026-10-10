class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first = 0
        second = first + 1
        
        n = len(s)
        count = 1
        if n<2:
            return n
        hs = set(s[first])
        while first < n and second <= n - 1:
            while s[second] in hs:
                hs.remove(s[first])
                first+=1
            hs.add(s[second])
            count = max(second-first+1,count)
            second = second + 1


            
        return count