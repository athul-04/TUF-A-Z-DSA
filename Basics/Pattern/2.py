class Solution:
    def pattern2(self, n):

        for i in range(0,n):
            for j in range(0,i+1):
                print("*",end="")
            print(end="\n")