    """
    create a new array
    append the existing numbers to the array
    append the n+i element to next to the appended number
    O(N)
    """

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp_nums= []
        for i in range(0,len(nums)-n,1):
            temp_nums.append(nums[i])
            temp_nums.append(nums[n+i])
        return temp_nums
