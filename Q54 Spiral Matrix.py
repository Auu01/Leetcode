class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Doesn't work expected, need fix
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        res = []
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for j in range(top, bottom):
                res.append(matrix[j][right - 1])
            right -= 1
            if left < right:
                for a in range(right, left, -1):
                    res.append(matrix[bottom - 1][a - 1])
                bottom -= 1
            if top < bottom:
                for b in range(bottom, top, -1):
                    res.append(matrix[b - 1][left])
                left += 1
        return res


