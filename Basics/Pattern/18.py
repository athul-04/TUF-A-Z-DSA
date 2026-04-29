class Solution:
    def pattern18(self, n):

        for i in range(1,n+1):  
            pt=n-i
            for j in range(0,i):
                print(chr(65+pt+j),end="")
            print(end="\n")


testCase=Solution().pattern18(5)