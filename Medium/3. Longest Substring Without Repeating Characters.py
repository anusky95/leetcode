

class Solution:
    
    def check_duplicate(self,str_a):
        unique_set = set()
        if len(str_a)==1:
            return 1
        else:
            for i in str_a:
                if i in unique_set:
                    return 0
                unique_set.add(i)
        return len(unique_set)
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        else:
            s0=s[0]
            if all(c == s0 for c in s[1:]) == True:
                return 1
            sub_dict={}
            list_len=[]
            for i in range(0,len(s)-1):
                for j in range(i+1,len(s)):
                    #check if it has duplicate characters and get the length add to dict
                    # get the highest length in dict
                    res = self.check_duplicate(s[i:j+1])
                    list_len.append(res)
            if len(list_len)==0:
                return 0
            else:
                return max(list_len)
