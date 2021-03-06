"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5

"""



class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        reslist=[]
        for i in range(len(arr)):
            if i==(len(arr)-1):
                reslist.append(-1)
            else:
                reslist.append(max(arr[i+1:]))
        return reslist
    
    
    """
    Faster Solution : Beats 100%
    
     maxNum = -1
        for i in range(len(arr) - 1, -1, -1):
            last = maxNum
            maxNum = max(maxNum, arr[i])
            arr[i] = last
        return arr
    
    
    """
    
