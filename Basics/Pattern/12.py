class Solution:
    def pattern12(self, n):
        
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end="")
            for k in range(0,2*n-(2*i)):
                print(" ",end="")
            for z in range(i,0,-1):
                print(z,end="")
            print(end="\n")

testCase=Solution().pattern12(5)