class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_index = 0
        end_index = len(numbers) - 1
        while(start_index<end_index):
            if target > (numbers[start_index]+numbers[end_index]):
                start_index = start_index + 1
            elif target < (numbers[start_index]+numbers[end_index]):
                end_index = end_index - 1
            else:
                break
                # return [start_index+1,end_index+1]
        return [start_index+1,end_index+1]