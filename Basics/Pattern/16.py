class Solution:
    def pattern16(self, n):

        for i in range(n):
            for _ in range(0,i+1):
                print(chr(65+i),end="")
            print(end="\n")



testCase=Solution().pattern16(5)
