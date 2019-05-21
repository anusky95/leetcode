class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        """
        case 1: if the target is found, immediately return the index
        case 2: if target is not found, use binary search and insert after the low value. 
        
        """
        # Target is found in the array
        if target in nums:
            return nums.index(target)

        # Target is not found and use binary search to find the nearest index after which 
        # target should be inserted.
        
        else:
            
            l = 0
            h = len(nums)-1
            while l <= h:
                mid = l+(h-l)//2
                if nums[mid]==target:
                    return mid
                elif target>nums[mid]:
                    l = mid + 1
                else:
                    h = mid-1
            return l
