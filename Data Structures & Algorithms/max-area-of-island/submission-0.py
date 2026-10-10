class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        neighbours = [(-1,0),(0,-1),(1,0),(0,1)]
        max_area = 0
        self.count = 0
        
        def dfs(r,c):
            if not (0<=r<row and 0<=c<col): return 
            if grid[r][c]==0: return 
            
            grid[r][c]=0
            self.count+=1
            for n in neighbours:
                dfs(r+n[0],c+n[1])
            # print(self.count,r,c,grid[r][c])
            return 
        
        for i in range(row):
            for j in range(col):
                dfs(i,j)
                max_area = max(self.count,max_area)
                self.count = 0
            
                    
        return max_area 




        