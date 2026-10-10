class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table_s = [0]*26
        hash_table_t = [0]*26

        if len(s)!=len(t):
            return False

        for char in s:
            hash_table_s[ord(char)-ord('a')]+=1

        for char in t:
            hash_table_t[ord(char)-ord('a')]+=1

        return hash_table_s==hash_table_t




        