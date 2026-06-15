class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix)*len(matrix[0])-1
        while low<=high:
            ndx = (low+high)//2
            row = int(ndx/len(matrix[0]))
            col = ndx%len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = ndx + 1
            else:
                high = ndx - 1
        return False
        