class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        new_list= [1] * n

        prod = 1
        for i in range(0, n):
            new_list[i] = prod
            prod*= nums[i]
        prod = 1
        for i in range(n-1,-1,-1):
            new_list[i] =new_list[i]* prod
            prod*= nums[i]
        return new_list

