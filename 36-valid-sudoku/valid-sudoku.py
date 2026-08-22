class Solution(object):
    def isValidSudoku(self, board):
        # check row
        for i in range(9):
            row = set()
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if num in row:
                        return False
                    row.add(num)

        #check coloum
        for i in range(9):
            col = set()
            for j in range(9):
                num = board[j][i]
                if num != '.':
                    if num in col:
                        return False
                    col.add(num)
                
        #check Box
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                box = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        num = board[i][j]

                        if num != '.':
                            if num in box:
                                return False
                            box.add(num)

        return True