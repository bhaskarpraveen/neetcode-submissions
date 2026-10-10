class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for num in nums:
            hash_set.add(num)
        
        return len(hash_set)!=len(nums)