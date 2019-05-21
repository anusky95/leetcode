class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        case 1: if number is negative return False
        case 2: use the brute force reversal method
        """
        if x<0:
            return False
        
        else:
            rev = 0
            num = x
            while num>0:
                rem = num%10
                rev = rev * 10 + rem
                num = num//10
            if rev == x:
                return True
            else:
                return False
            
        """
        Time complexity : We divide the input by 10 for every iteration, so the time
        complexity is O(log10(n)).
        
        Space complexity: O(1)
        
        """
