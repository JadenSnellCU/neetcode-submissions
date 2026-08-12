
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        up = 0
        down = rows-1
        while up <= down:
            mud = (up+down)//2
            if matrix[mud][0]> target:
                down = mud-1
            elif matrix[mud][-1]<target:
                up = mud+1
            else:
                left = 0
                right = cols-1
                while left <= right:
                    mlr = (left+right)//2
                    if matrix[mud][mlr] == target:
                        return True
                    elif matrix[mud][mlr] > target:
                        right = mlr-1
                    else:
                        left = mlr+1
                return False
        return False