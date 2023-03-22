class Solution1(object):
    def isInbound(self, i, j, R, C, visited):
        return 0 <= i < R and 0 <= j < C and visited[i][j] == 0 

    def updateMatrix(self, mat):
        R = len(mat)
        if R == 0:
            return mat
        C = len(mat[0])
        
        q = []
        visited = [[0] * C for r in range(R)]
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    visited[i][j] = 1
                    q.append([i, j])

        X = [1, 0, -1, 0]
        Y = [0, 1, 0, -1]
        while len(q) != 0:
            cr, cc = q.pop(0)
            for i in range(4):
                newR, newC = cr + X[i], cc + Y[i]
                if self.isInbound(newR, newC, R, C, visited) and mat[newR][newC] == 1:
                    visited[newR][newC] = 1
                    mat[newR][newC] = 1 + mat[cr][cc]
                    q.append([newR, newC])
        return mat

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        out = [row[:] for row in mat]
        R, C = len(mat), len(mat[0])
        def dfs(r, c, sr, sc):
            if mat[r][c] == 0:
                return 0
            if r >= 1 and r-1 != sr:
                up = 1 + dfs(r-1, c, sr, sc)
            else:
                up = 9999999
            if r+1 < R and r+1 != sr:
                down = 1 + dfs(r+1, c, sr, sc)
            else:
                down = 99999999
            if c >= 1 and c-1 != sc:
                left = 1 + dfs(r, c-1, sr, sc)
            else:
                left = 99999999
            if c+1 < C and c+1 != sc:
                right = 1 + dfs(r, c+1, sr, sc)
            else:
                right = 9999999
            return min(up, down, left, right)
        
        i = j = 0
        while i < R:
            j = 0
            while j < C:
                out[i][j] = dfs(i, j, i, j)
                j += 1
            i += 1
        return out

s = Solution1()
a = [[0,0,0],[0,1,0],[1,1,1]]
print(s.updateMatrix(a))