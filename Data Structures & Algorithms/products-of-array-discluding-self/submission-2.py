class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = [1]
        temp_number = nums[0]
        for number in range(0,len(nums)):
            if number == 0:
                continue
            else:
                solution.append(temp_number)
            temp_number = temp_number * nums[number]
            print(temp_number)
        print(solution)
        temp_number = 1
        for number in range(len(nums)-1,-1,-1):
            print(number)
            solution[number] = solution[number] * temp_number
            temp_number = temp_number * nums[number]
            # print(solution[number])
        return solution