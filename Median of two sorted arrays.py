class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        """
        :type nums1: int
        :type nums2: int
        :rtype: float
        """
        
        #declaring an empty list
        newarr=[]
        
        #traversing the two lists to collect the numbers and store it in the new list
        for i in nums1:
            newarr.append(i)
        for j in nums2:
            newarr.append(j)
            
        #sorting the new list 
        newarr = sorted(newarr)
        
                
        l = len(newarr)

        # if it is even length list get the middle number by taking median of the middle two numbers
        if l%2==0:
            mid = newarr[int(l/2)]+newarr[int((l-1)/2)]
            res = mid/2
            
        # if it is odd length list get the middle number directly
        else:
            res = newarr[int((l-1)/2)]
        return res
            
