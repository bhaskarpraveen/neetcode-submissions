class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i,a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            j = i + 1
            k = n - 1
            while(j<k ):
                if a + nums[j] + nums[k] == 0:
                    # if not [a,nums[j],nums[k]] in res:
                    res.append([a,nums[j],nums[k]])
                    j = j+1
                    k = k-1
                    while j <k and nums[j] == nums[j-1]:
                        j = j + 1
                    while j<k and nums[k] == nums[k+1]:
                        k = k - 1
                elif a + nums[j] + nums[k] > 0:
                    k = k-1
                    continue
                else :
                    j = j + 1
        return res



        