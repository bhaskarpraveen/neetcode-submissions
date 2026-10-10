class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = start + 1
        max_vol = 0
        while(start < len(heights)-1):
            vol = min(heights[start],heights[end])*(end - start)
            if vol > max_vol:
                max_vol = vol
            if end == len(heights) - 1:
                start = start + 1
                end = start + 1
            else:
                end = end + 1
        return max_vol

