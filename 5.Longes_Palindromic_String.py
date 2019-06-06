class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_str = ""
        for ind,val in enumerate(s):
            current = val
            if len(current)>len(longest_str):
                longest_str=current
            for inind,inval in enumerate(s[ind+1:]):
                current+=inval
                if current==current[::-1]:
                    if len(current)>len(longest_str):
                        longest_str=current
        return longest_str
        
