class Solution:
    def pattern19(self, n):

        for i in range(0,2*n):
            if i>=n:
                i=(2*n-1)-i
            for _ in range(0,n-i):
                print("*",end="")
            for _ in range(0,2*i):
                print(" ",end="")
            for _ in range(0,n-i):
                print("*",end="")

            print(end="\n")



        pass

5- 4
6 -3
7-2
8 - 1
9- 0




testCase=Solution().pattern19(2)