class Solution:
    def solve(self, board):
        h = len(board)
        if h == 0:
            return
        w = len(board[0])

        #找到外围的0和内圈的0
        inner_0 = []
        outer_0 = []
        for i in range(h):
            for j in range(w):
                if (i > 0 and i < h - 1) and (j > 0 and j < w - 1) and board[i][j] == 'O':
                    inner_0.append((i,j))
                elif board[i][j] == 'O':
                    outer_0.append((i,j))
        #print(inner_0)
        #print(outer_0)
        #对每个外圈0遍历，找到相邻的0
        for (i,j) in outer_0:
            if (i,j) in [(0,0),(0,w),(h,0),(w,h)]:
                continue
            if i == 0:
                if (i+1,j) in inner_0:
                    outer_0.append((i+1,j))
                    #outer_0.remove((i,j))
                    inner_0.remove((i+1,j))
            elif i == h:
                if (i-1,j) in inner_0:
                    outer_0.append((i-1,j))
                    #outer_0.remove((i,j))
                    inner_0.remove((i-1,j))
            elif j == 0:
                if (i,j+1) in inner_0:
                    outer_0.append((i,j+1))
                    #outer_0.remove((i,j))
                    inner_0.remove((i,j+1))
            elif j == w:
                if (i,j-1) in inner_0:
                    outer_0.append((i,j-1))
                    #outer_0.remove((i,j))
                    inner_0.remove((i,j-1))
            else:
                near = [(i,j-1),(i,j+1),(i-1,j),(i+1,j)]
                for n in near:
                    if n in inner_0:
                        outer_0.append(n)
                        inner_0.remove(n)
        for (m,n) in inner_0:
            board[m][n] = 'X'

board = [['X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['X', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'X']]
# board = [["X","X","X","X"],
#          ["X","O","O","X"],
#          ["X","X","O","X"],
#          ["X","O","X","X"]]
Solution().solve(board)
print(board)

