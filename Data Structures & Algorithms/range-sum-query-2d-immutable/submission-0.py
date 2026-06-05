class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # zeroes offset
        rows, col = len(matrix), len(matrix[0])
        self.m = [[0] * (col + 1) for _ in range(rows + 1)]

        # prefix sum creation
        for r in range(rows):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                above = self.m[r][c + 1]
                self.m[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomright = self.m[row2][col2]
        above = self.m[row1 - 1][col2]
        topleft = self.m[row1 - 1][col1 - 1]
        left = self.m[row2][col1 - 1]

        return bottomright - above - left + topleft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)