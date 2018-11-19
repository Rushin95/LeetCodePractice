class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        def scan(i,j,grid):
            if 0 <= i < rows and 0 <= j < cols:
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    scan(i+1,j,grid)
                    scan(i-1,j,grid)
                    scan(i,j+1,grid)
                    scan(i,j-1,grid)
            return 1
                    
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    scan(i,j,grid)
        return count
        