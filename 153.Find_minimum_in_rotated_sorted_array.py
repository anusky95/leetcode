class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        """
        :type nums: list
        :rtype: int
        """
        
        #Set the first number of the list as min value
        minval = nums[0]
        
        #Compare each value of the array with the minvalue and swap if the number is lesser than minvalue
        for i in range(1,len(nums)):
            if nums[i]<minval:
                minval = nums[i]
            else:
                pass
        return minval 
    
        #Algorithm complexity
        # O(N) where N is the size of the array 
        
        # The code can also be written in a one liner pythonic style 
        # by directly having the following statement in the function
        # return min(nums)
