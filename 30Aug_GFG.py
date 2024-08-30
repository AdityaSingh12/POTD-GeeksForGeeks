"""
The n-queens puzzle is the problem of placing n queens on a (n×n) 
chessboard such that no two queens can attack each other.
Given an integer n, find all distinct solutions to the n-queens puzzle. 
Each solution contains distinct board configurations of the n-queens placement, 
where the solutions are a permutation of [1,2,3..n] in increasing order, 
here the number in the ith place denotes that the ith-column queen is placed in the row with that number. 
For eg below figure represents a chessboard [3 1 4 2].
"""

class Solution:
    def __init__(self):
        self.result = []
        self.row = [0] * 10
    
    def place(self, r, c):
        for prev in range(c):
            if self.row[prev] == r or abs(self.row[prev] - r) == abs(prev - c):
                return False
        return True

    def bt(self, c, n):
        if c == n:
            self.result.append([self.row[i] + 1 for i in range(n)])
            return
        for i in range(n):
            if self.place(i, c):
                self.row[c] = i
                self.bt(c + 1, n)

    def nQueen(self, n):
        self.result = []
        self.bt(0, n)
        return self.result
    
    #driver code

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()