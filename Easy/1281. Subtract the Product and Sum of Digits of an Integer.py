class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """
        Runtime: 28 ms, faster than 74.85% of Python3 online submissions for Subtract the Product and Sum of Digits of an         Integer.
        Memory Usage: 14 MB, less than 99.95% of Python3 online submissions for Subtract the Product and Sum of Digits of         an Integer.
        
        Explanation:
        Convert the number to string and find the product and the sum.
        
        Time Complexity
        O(N)
        
        """
        
        prod = 1
        sums = 0
        for i in str(n):
            prod*=int(i)
            sums+=int(i)
        return prod-sums
