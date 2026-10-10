class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total = 0
        start = 0
        end = len(heights)-1
        while start<end:
            vol = min(heights[start],heights[end])* (end-start)
            total = max(total,vol)
            if heights[start]<heights[end]:
                start+=1
            else:
                end-=1
        return total

