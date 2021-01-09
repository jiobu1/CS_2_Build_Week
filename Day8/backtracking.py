"""
On a 2-dimensional grid, there are 4 types of squares:

    1 represents the starting square.  There is exactly one starting square.
    2 represents the ending square.  There is exactly one ending square.
    0 represents empty squares we can walk over.
    -1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:
Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:
Input: [[0,1],[2,0]]
Output: 0
Explanation:
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Note:
    1 <= grid.length * grid[0].length <= 20

"""
class Solution:
    """
    Plan:
    - Traverse the maze
    - pass x, y coordinates to helper function
    - recurse in four directions (up, down, left, right)
      to try out all possible routes

    Backtrack if:
    1. if we're stuck
    2. we're at the goal square, but haven't visited all vaild cells yet
    3. outside the boundaries of the maze
    4. if you're at an obstacle square -1

    We can count a solution if we're at the goal square and we've visited all valid squares
    """
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        startingPoint = self.findStartingPoint(grid)

        if startingPoint == None:
            return 0
        self.uniquePathsIIIHelper(grid, startingPoint[0], startingPoint[y])
        return self.res

    def uniquePathsIIIHelper(grid, x, y):
        width, height = len(grid[0], len[grid])
        if x < 0, or x >= width or y < 0 or y >= height or grid[y][x] == -1:
            return
        if grid[y][x] == 2:
            for j in range(width):
                if grid[i][j] == 0:
                    return


    # Returns (x, y) of the starting point in the grid
    def startingPoint(grid):
            # TODO