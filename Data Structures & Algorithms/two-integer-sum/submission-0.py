class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()

        for i in range(0,len(nums)):
            if nums[i] in  hash_table:
                return [hash_table[nums[i]],i]
            hash_table[target-nums[i]] = i

        