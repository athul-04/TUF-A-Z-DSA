class Solution:
    def printNumbers(self, n):
        if n==1:
            print(n)
            return
        self.printNumbers(n-1)
        print(n)


testCase=Solution().printNumbers(20)