class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        d = {}
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                d[(i, j)] = d.get((i, j - 1), 0) + d.get((i - 1, j), 0) - d.get((i - 1, j - 1), 0) + num
        self.m = d


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        br = self.m[(row2, col2)]
        l = self.m.get((row2, col1 - 1), 0)
        u = self.m.get((row1 - 1, col2), 0)
        tl = self.m.get((row1 - 1, col1 - 1), 0)
        return br - l - u + tl
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)