/*
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
*/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        
        MOST FAVORITE SO FAR
        :param nums: Array of integers
        :returns res: Integer
        
        Max sum of contiguous numbers
        Pseudocode:
        Outer loop which reads all the nums
        inner loop which traverses one by one adding to the outer loop number
        return the max
        O(N2)
        
        -2,1,-3,4,-1,2,1,-5,4
        find highest number and its index
        add the numbers before this maxnum and also the numbers after it one by one and check which yields highest result
        
        
        highestnum + [highestnunindex: ]
        [:highestnum] + [indhighestnum]
        []
        MY approach - undone
        
        maxnum = max(nums)
        maxind = nums.index(maxnum)
        lsum=maxnum
        i=0
        while i<nums[maxind]-1:
            if lsum>maxnum:
                return lsum
            else:
                lsum+=nums[i]
            i=i+1
        lsum=maxnum            
        for i in range(maxind,len(nums)):
          
            if lsum>maxnum:
                print(lsum)
                maxnum = lsum
            else:
                lsum+=nums[i]
        return maxnum
        
        """
        
        ## Kadane's algorithm
        ## Compare the current number with the sum so far, if the current number is bigger than sum so far max picks that and leaves 
        ##behind all addition until then
            
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            print(curr_sum)
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
