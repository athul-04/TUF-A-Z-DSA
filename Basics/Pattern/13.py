class Solution:
    def pattern13(self, n):
        inc=1
        for i in range(n):
            for _ in range(0,i+1):
                print(inc,end="")
                inc+=1
            print(end="\n")



testCase=Solution().pattern13(5)

