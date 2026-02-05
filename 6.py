# Solution 1 : 2D array

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        mat = [[] for _ in range(numRows)]
        i = 0
        n = len(s)
        while i < n:
            for down in range(numRows):
                if i < n:
                    mat[down].append(s[i])
                    i += 1
            for up in range(numRows - 2, 0, -1):
                if i < n:
                    mat[up].append(s[i])
                    i += 1
        ans = ""
        for row in mat:
            ans += ''.join(row)
        return ans

# Solution 2: Two pointers (Optimal)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        a=""
        for i in range(numRows):
            for j in range(i,len(s),2*(numRows-1)):
                a+=s[j]
                if(i>0 and i<numRows-1 and j+2*(numRows-1)-2*i < len(s)):
                    a+=s[j+2*(numRows-1)-2*i]
        return a
