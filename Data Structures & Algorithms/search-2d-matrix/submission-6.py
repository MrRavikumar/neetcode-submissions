class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute Force
        # row = len(matrix)
        # col = len(matrix[0])
        # for m in range(row):
        #     for n in range(col):
        #         if matrix[m][n] == target:
        #             return True
        
        # return False

        # Binary Search
        # def binarySearch(arr, target):
        #     l, r = 0, len(arr)-1
        #     while l <= r:
        #         m = ( l + r ) // 2
        #         if arr[m] == target:
        #             return True
        #         elif arr[m] < target:
        #             l = m + 1
        #         elif arr[m] > target:
        #             r = m - 1
            
        #     return False
        
        # n = len(matrix)
        # m = len(matrix[0])
        # for i in range(n):
        #     if matrix[i][0] <= target <= matrix[i][m-1]:
        #         return binarySearch(matrix[i], target)
        # return False

        #Optimized Approach
        n = len(matrix)
        m = len(matrix[0])

        l, r = 0, (n*m)-1
        
        while l <= r:
            mid = ( l + r ) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else: 
                r = mid - 1
        
        return False



        

