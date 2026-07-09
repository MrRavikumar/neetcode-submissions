class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute Force
        row = len(matrix)
        col = len(matrix[0])
        for m in range(row):
            for n in range(col):
                if matrix[m][n] == target:
                    return True
        
        return False
