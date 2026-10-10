class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])

        count = 0
        b = [(-1,0),(0,-1),(1,0),(0,1)]

        def dfs(row,col):
            if not (0<=row<r and 0<=col<c): return 0
            if grid[row][col]=="0": return 0

            grid[row][col]="0"

            for add in b:
                dfs(row+add[0],col+add[1])
            return 1
            

        for i in range(r):
            for j in range(c):
                if dfs(i,j):
                    count+=1
                    


        return count






        