class Solution:
    def maxArea(self, heights: List[int]) -> int:
        num = len(heights)
        first = 0
        second = num-1
        max_water = 0
        while(first<second):
            vol = min(heights[first],heights[second])* (second-first)
            
            max_water = max(max_water,vol)
            if heights[first]<heights[second]:
                first+=1
            else:
                second-=1
        return max_water
            


