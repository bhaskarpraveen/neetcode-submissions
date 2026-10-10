class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        left = 0
        right = 0
        if len(s)<2:
            return len(s)
        count = 1

        while(right<len(s)):
            dis = right-left + 1
            if s[right] not in hash_set:
                hash_set.add(s[right])
                if  dis>count:
                    count = dis
                right = right + 1
            else:
                left = left +1
                right = left
                hash_set = set()
        return count


        