class Solution:
    def pattern17(self, n):
        
        for i in range(1,n+1):

            for _ in range(0,n-i):
                print(" ",end="")
            for j in range(0,n-(n-i)):
                print(chr(65+j),end="")
            for k in range(n-(n-i)-2,-1,-1):
                print(chr(65+k),end="")
            for _ in range(0,n-i):
                print(" ",end="")

            print(end="\n")

testCase=Solution().pattern17(5)