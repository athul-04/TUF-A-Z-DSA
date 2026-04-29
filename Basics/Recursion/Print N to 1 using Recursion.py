class Solution:
    def printNumbers(self, n):
        if n==1:
            print(n,end="\n")
            return
        print(n,end="\n")
        self.printNumbers(n-1)


testCase=Solution().printNumbers(10)