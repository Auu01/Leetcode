class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left=0
        right=n-1
        top=0
        bottom=n-1
        matrix=[[0] * n for _ in range(n)]
        num=1
        while left <= right and top <= bottom:
            for i in range(left,right+1,1):
                matrix[top][i]=num
                num += 1
            top += 1
            for j in range(top,bottom+1,1):
                matrix[j][right]=num
                num += 1
            right -= 1
            if top <= bottom:
                for n in range(right,left-1,-1):
                    matrix[bottom][n]=num
                    num += 1
                bottom -= 1
            if left <= right:
                for m in range(bottom,top-1,-1):
                    matrix[m][left]=num
                    num += 1
                left += 1
        return matrix



