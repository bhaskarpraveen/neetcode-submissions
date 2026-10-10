class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for i in range(0,len(nums)): 
            count = 0
            if nums[i]-1 not in num_set:
                while nums[i]+count in num_set: 
                    count+=1
            longest = max(longest,count)
        return longest


                