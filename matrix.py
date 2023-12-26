# Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.

"""
# iterate matrix to find rows and colums containg zeros

# iterate that rows and columns where zero is present and make them all zero

# TIME: O(MxN), M is th e number of rows and N is the number of columns
# SPACE: O(M+N)
"""


class Matrix:
    def setZeros(self, matrix):
        if not matrix or not matrix[0]:
            return
        rows, cols = len(matrix), len(matrix[0])

        row_zero, col_zero = set(), set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)

        # set that row to zero
        for row in row_zero:
            for j in range(cols):
                matrix[row][j] = 0

        # set that column to zero
        for col in col_zero:
            for j in range(rows):
                matrix[j][col] = 0
        print("Modified: ")
        for row in matrix:
            print(row)


ans = Matrix()

# Test Case 1: No Zeros
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans.setZeros(matrix1)

# Test Case 2: Zeros in Rows and Columns
matrix2 = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]

# Test Case 3: Zeros in First Row and Column
matrix3 = [[0, 2, 3], [4, 5, 6], [7, 8, 9]]
ans.setZeros(matrix3)

# Test Case 4: Zeros in Last Row and Column
matrix4 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
ans.setZeros(matrix4)

# Test Case 5: Empty Matrix
matrix5 = []
ans.setZeros(matrix5)

# Test Case 6: Single Element Matrix
matrix6 = [[0]]
ans.setZeros(matrix6)
