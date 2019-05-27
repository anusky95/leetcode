class Solution:
    def isAnagram(self, s: str, t: str) -> bool:\
        
        # Sort both the strings to make character by character comparison
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        
        pos = 0
        i = 0
        anagramVal = False
        lens = len(s)
        lent = len(t)
        
        # If length of s and t are not same then they are not anagrams
        if lens == lent:
            
            # While length of s is less than t
            while pos < lens and not anagramVal:
                
                # If the characters comparison is successful increment
                if s[i]==t[i]:
                    i=i+1
                else:
                    anagramVal = False
                    return anagramVal
                pos = pos+1
            return True
        else:
            return False
                
