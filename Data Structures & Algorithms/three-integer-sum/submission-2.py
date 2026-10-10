class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        first_index = 0
        second_index = 1
        result = []
        while(first_index<len(nums)):
            if second_index == first_index:
                if second_index < len(nums)-1:
                    second_index = second_index+1
                else:
                    second_index = 0
                    first_index = first_index +1
            if first_index == len(nums)-1:
                break
            if ((nums[first_index] + nums[second_index])* -1) in nums:
                for i in range(0,len(nums)):
                    if i == first_index or i == second_index:
                        continue
                    if (nums[i] == ((nums[first_index] + nums[second_index])* -1)) and (i !=first_index and i!=second_index):
                        if not ([nums[first_index],nums[second_index],nums[i]] in result or [nums[first_index],nums[i],nums[second_index]] in result or [nums[second_index],nums[first_index],nums[i]] in result or [nums[second_index],nums[i],nums[first_index]] in result or [nums[i],nums[second_index],nums[first_index]] in result or [nums[i],nums[first_index],nums[second_index]] in result):
                            result.append([nums[first_index],nums[second_index],nums[i]])

            if second_index == len(nums)-1:
                second_index = 0
                first_index = first_index +1
            else:
                second_index = second_index + 1
            if first_index == len(nums)-1:
                break
        return result

