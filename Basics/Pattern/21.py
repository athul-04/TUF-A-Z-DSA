class Solution:
    def pattern21(self, n):

        for i in range(n):

            if i in (0,n-1):
                for _ in range(n):
                    print("*",end="")
                print(end="\n")
                continue
            print("*",end="")
            for _ in range(0,n-2):
                print(" ",end="")
            print("*",end="\n")







testCase=Solution().pattern21(5)