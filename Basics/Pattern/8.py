class Solution:
    def pattern8(self, n):

        for i in range(0,n):
            for j in range(0,i):
                print(" ",end="")
            for k in range(0,(2*n)-1-(2*i)):
                print("*",end="")
            
            print(end="\n")






test=Solution()

test.pattern8(5)