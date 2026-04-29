class Solution:
    def pattern15(self, n):

        for i in range(n):
            for j in range(0,n-i):
                print(chr(65+j),end=" ")
            print(end="\n")

testCase=Solution().pattern15(5)