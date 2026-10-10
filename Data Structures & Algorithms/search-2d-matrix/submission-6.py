class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        if nums[start] == target or nums[end]==target:
            return True
        while(start<end and start!=end):
            if nums[start] == target or nums[end]==target:
                return True

            mid = (start+end)//2
            if start == mid or end == mid:
                break
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                end = mid
            else:
                start = mid

        if nums[start] == target or nums[end]==target:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_s = 0
        end_s = len(matrix)-1
        m_len = len(matrix[0])-1
        if start_s == end_s:
            return self.search(matrix[start_s],target)
        while(start_s<end_s and start_s!= end_s ):
            if start_s+1 == end_s and matrix[start_s][m_len]<target and matrix[end_s][0]>target:
                return False
            if target == matrix[start_s][0] or target == matrix[start_s][m_len]:
                return True
            if target == matrix[end_s][0] or target == matrix[end_s][m_len]:
                return True
            if target> matrix[start_s][0] and target<matrix[start_s][m_len]:
                return self.search(matrix[start_s],target)
            if target> matrix[end_s][0] and target<matrix[end_s][m_len]:
                return self.search(matrix[end_s],target)
            mid = (start_s+end_s)//2

            if start_s == mid or end_s == mid:
                break
            if target == matrix[mid][0] or target == matrix[mid][m_len]:
                return True
            elif target> matrix[mid][0] and target<matrix[mid][m_len]:
                return self.search(matrix[mid],target)
            elif target<matrix[start_s][0]:
                end_s = mid
            else:
                start_s = mid
        return False





                    


        