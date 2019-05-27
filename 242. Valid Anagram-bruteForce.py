class Solution:
    def isAnagram(self, s: str, t: str) -> bool:\
        
        # Sort both the strings to make character by character comparison
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        
        pos = 0
        anagramVal = False
        lens = len(s)
        lent = len(t)
        
        # If length of s and t are not same then they are not anagrams
        if lens == lent:
            # While length of s is less than t
            while pos < lens and not anagramVal:
                
                # If the characters comparison is successful increment
                if s[pos]==t[pos]:
                    pos=pos+1
                else:
                    anagramVal = False
                    return anagramVal
            return True
        else:
            return False
                
    """
        Time Complexity : Sorting the two strings = O(N^2)
        Space Complexity : We are not using additional data structures here hence it is 
    """
