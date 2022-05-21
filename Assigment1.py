​class Solution: 
 ​    def singleNumber(self,nums): 
 ​        sum=0 
 ​        for i in nums: 
 ​            sum=i^sum 
 ​        return sum
