class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)

        for i in range(1,len(lis)):
            sub = [ lis[k] for k in range(0,i+1) if nums[k]<nums[i]]
            lis[i] = 1+max(sub,default=0)
        return max(lis)
        
        