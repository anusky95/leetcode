class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ### If the length of list is 0 then return 0 
        if len(nums)<0:
            return 0
        else:
        ### Convert the list to set to remove duplicates 
                sortnums = list(set(nums))
        ### Sort in descending order
                sortnums = sorted(sortnums,reverse=True)
        ### If there are atleast 3 numbers return the third number else return the max number
                if len(sortnums)>=3:
                    return sortnums[2]
                else:
                    return max(nums)

        
        
