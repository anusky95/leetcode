class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Submission Stats
        Runtime: 32 ms, faster than 73.40% of Python3 online submissions for Number of Good Pairs.
        Memory Usage: 14.1 MB, less than 99.99% of Python3 online submissions for Number of Good Pairs.
        
        Explanation:
        If the list contains 0 or 1 number return 0
        Else : Compare every element with each other and check for the two conditions mentioned.
            if both these conditions are satisfied increase the counter by 1 each time
        return counter
        
        :param nums: List of numbers 
        :return count_num: Count of identical pairs which satisfy condition
        
        
        """
        
        if len(nums)==0 or len(nums)==1:
            return 0
        else:
            count_num=0
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if (nums[i]==nums[j]) and i<j:
                        count_num+=1
            return count_num

        
        """
        Alternative solutions
        count the previous occurences of the number and increment every time it occurs
           
           Optimized O(N)
           
            dic = {}
            count =0
        
            for num in nums:
                if num in dic:
                    count +=dic[num]
                    dic[num] +=1
                else:
                    dic[num] =1
            return count
         
         
         
         --------------------------------------------------------------------
         
            Optimized O(N) Without if else 
         
            counts=0
            my_dict={}
            for n in nums:
                counts+=my_dict.get(n,0)
                my_dict[n]=my_dict.get(n,0)+1
        
        
        """
      
    
