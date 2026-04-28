class Solution:
    def pattern9(self, n):
        for i in range(0,2*n):
            if i>=n:
                i=(2*n-1)-i
            for _ in range(0,n-1-i):
                print(" ",end="")
            for _ in range(0,2*(i)+1):
                print("*",end="")
            print(end="\n")

testCase=Solution()
testCase.pattern9(2)