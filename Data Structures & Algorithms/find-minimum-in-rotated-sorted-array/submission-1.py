class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums)-1
        if nums[s]<nums[e]:
            return nums[s]
        if len(nums)==1:
            return nums[0]
        while(s<e and s!=e):
            m = (s+e)//2
            if nums[m]>nums[e]:
                s = m
            else:
                e = m
            if s+1==e and nums[s]>nums[e]:
                return nums[e] 