class Solution:
    def pattern20(self, n):

        for i in range(0,2*n-1):
            if i>=n:
                i=(2*n-1)-i-1
            for _ in range(0,i+1):
                print("*",end="")
            for _ in range(0,2*n-(2*(i+1))):
                print(" ",end="")
            for _ in range(0,i+1):
                print("*",end="")
            print(end="\n")



        pass






testCase=Solution().pattern20(5)