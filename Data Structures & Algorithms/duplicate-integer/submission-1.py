class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()
        flag = False
        for number in nums:
            if number in seen_set:
                flag = True
                break
            seen_set.add(number)
        return flag

        