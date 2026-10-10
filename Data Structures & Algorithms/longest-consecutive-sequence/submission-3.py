class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        max_count = 1
        count = 1
        for number in range(0,len(nums)-1):
            if nums[number + 1] == nums[number]:
                    continue
            elif nums[number + 1] - nums[number] == 1:
                count = count + 1
            else:
                count = 1
            if max_count < count :
                 max_count = count
        return max_count