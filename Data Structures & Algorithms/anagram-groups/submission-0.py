class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)

        for string in strs:
            hash_list = [0]*26
            for char in string:
                hash_list[ord(char)-ord('a')]+=1
                
            hash_table[tuple(hash_list)].append(string)
        result=[]
        for i in hash_table:
            result.append(hash_table[i])
        return result