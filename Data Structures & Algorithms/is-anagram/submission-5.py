class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table_s = [0]*26
        hash_table_t = [0]*26
        if len(s)!=len(t):
            return False
        for char in range(0,len(s)):
            hash_table_s[ord(s[char])-ord('a')]+=1
            hash_table_t[ord(t[char])-ord('a')]+=1
        
        return hash_table_s == hash_table_t





        