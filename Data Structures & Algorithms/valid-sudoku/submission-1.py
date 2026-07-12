class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        myset = set()

        # row logic
        for r in range(9):
            for i in range(9):
                row_num = board[r][i]
                if row_num != ".":
                    if row_num in myset:
                        return False
                    myset.add(row_num)
            myset = set()

        # column logic
        for c in range(9):
            for i in range(9):
                col_num = board[i][c]
                if col_num != ".":
                    if col_num in myset:
                        return False
                    myset.add(col_num)
            myset = set()

        # 3x3 grid logic
        for a in range(0, 9, 3):
            for b in range(0, 9, 3):
                # 3x3 logic
                for g in range(3):
                    for h in range(3):
                        grid_num = board[a + g][b + h]
                        if grid_num != ".":
                            if grid_num in myset:
                                return False
                            myset.add(grid_num)
                myset = set()
        return True

        