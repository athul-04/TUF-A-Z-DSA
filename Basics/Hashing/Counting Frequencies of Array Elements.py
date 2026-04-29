
class Solution:
    def countFrequencies(self, nums):
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        
        ans=[]
        for key in d:
            ans.append([key,d[key]])
        return ans
        
