class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_table = dict()
        for num in nums:
            hash_table[num]=1+hash_table.get(num,0)
        bucket_list = [[] for i in range(len(nums)+1)]

        for num,cnt in hash_table.items():
            bucket_list[cnt].append(num)
        
        res = []
        for i in range(len(bucket_list)-1, -1, -1):
            for j in bucket_list[i]:
                res.append(j)
                if len(res)==k:
                    return res
        

        