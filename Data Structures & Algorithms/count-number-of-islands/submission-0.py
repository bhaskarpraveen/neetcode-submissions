class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        self.count = 0
        around = [(1,0),(0,-1),(-1,0),(0,1)]

        def dfs(row,col):
            if not (0<=row<r and 0<=col<c): return 0
            if grid[row][col] == "0": return 0
            if grid[row][col] == "": return 0
            
            if grid[row][col]=="1":
                grid[row][col]=""
            
                for add in around:
                    dfs(row+add[0],col+add[1])

            return 1
        
        for i in range(r):
            for j in range(c):
                self.count += dfs(i,j)

        return self.count



        