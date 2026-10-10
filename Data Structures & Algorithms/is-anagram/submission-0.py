class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_list = [0]*26

        for char in s:
            hash_list[ord(char)-ord('a')]-=1

        for char in t:
            hash_list[ord(char)-ord('a')]+=1
        
        for num in hash_list:
            if num!=0:
                return False
        return True

        