class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i,a in enumerate(nums):
            j = i + 1
            k = n - 1
            while(j<k ):
                if a + nums[j] + nums[k] == 0:
                    if not [a,nums[j],nums[k]] in res:
                        res.append([a,nums[j],nums[k]])
                elif a + nums[j] + nums[k] > 0:
                    k = k-1
                    continue
               
                j = j + 1
        return res



        