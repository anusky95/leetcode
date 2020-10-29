class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Runtime Efficiency : O(N^2)
        :param nums: List of ints
        :param target : Integer 
        : returns reslist: List of ints
        
        This function checks compares each pair of numbers in the list to check if they add up to the target.
        
        """
        res_list=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    res_list.append(i)
                    res_list.append(j)
        return res_list
