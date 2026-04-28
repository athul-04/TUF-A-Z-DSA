class Solution:
    def pattern11(self, n):
        temp=1
        for i in range(n):
            pt=temp
            for j in range(0,i+1):
                print(pt,end="")
                pt=0 if pt==1 else 1

            temp=0 if temp==1 else 1
            print(end="\n")

testCase=Solution().pattern11(5)