class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_list = [0]*26

        for char in range(0,len(s)):
            hash_list[ord(s[char])-ord('a')]-=1
            hash_list[ord(t[char])-ord('a')]+=1
        
        for num in hash_list:
            if num!=0:
                return False
        return True

        