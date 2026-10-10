class Solution:
    def rob(self, nums: List[int]) -> int:

        maxRob = [0]*len(nums)
        maxRob[0] = nums[0]
        for i in range(1,len(nums)):
            if i==1:
                maxRob[i] = max(nums[1],nums[0])
            else:
                maxRob[i] = max(nums[i]+maxRob[i-2],maxRob[i-1])
        
        return maxRob[len(nums)-1]
        