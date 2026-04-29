class Solution:   

    def palindromeCheck(self, s:str):
    
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j] :return False
            i+=1
            j-=1

        return True
    

testCase=Solution().palindromeCheck("aab")
print(testCase)