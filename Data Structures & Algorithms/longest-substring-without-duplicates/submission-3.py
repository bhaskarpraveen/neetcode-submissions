class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        left = 0
        right = 0
        if len(s)<2:
            return len(s)
        count = 0

        while(right<len(s)):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left = left+1
            hash_set.add(s[right])
            count = max(count,right - left + 1)
            right = right + 1
        return count


        