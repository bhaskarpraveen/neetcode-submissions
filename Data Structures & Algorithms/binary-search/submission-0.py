class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while(start<end and start!=end):
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end

            mid = (start+end)//2
            if start == mid or end == mid:
                break
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid
        
        
        if nums[start] == target:
                return start
        if nums[end] == target:
            return end
        return -1
        