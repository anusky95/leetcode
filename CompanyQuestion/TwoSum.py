class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Runtime Efficiency : O(N^2)
        :param nums: List of ints
        :param target : Integer 
        : returns reslist: List of ints
        
        This function checks compares each pair of numbers in the list to check if they add up to the target.
        
        
        res_list=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    res_list.append(i)
                    res_list.append(j)
        return res_list
        """
        
        """
         Runtime Efficiency : O(N)
         Complexity Analysis:

            Time complexity : O(n)O(n). We traverse the list containing nn elements only once. Each look up in the table costs only O(1)O(1) time.

            Space complexity : O(n)O(n). The extra space required depends on the number of items stored in the hash table, which stores at most nn elements.


         
         
        :param nums: List of ints
        :param target : Integer 
        : returns reslist: List of ints
        
        This function iterates through each number and checks if target - each number is already present if not then puts the number
        Iteration 0 : d[2] = 0
        Iteration 1: if 2 is present in dict:
                     return d[2],1
                     return 0,1
        """
        dicts={}
        for i,num in enumerate(nums):
            if target-num in dicts:
                return dicts[target-num],i
            dicts[num]=i
        
