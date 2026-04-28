class Solution:
    def pattern10(self, n):

        for i in range(1,2*n+1):
            if i>n:
                i=(2*n)-i
            for _ in range(i):
                print("*",end="")
            print(end="\n")

        pass

# 6- 4
# 7- 3
# 8- 2
# 9-1

testCase=Solution()

testCase.pattern10(5)