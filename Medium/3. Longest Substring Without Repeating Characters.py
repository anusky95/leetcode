class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        passes=0
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        else:
            result_list = []
            index_dict={}
            traverse = 0
            res_set = set()
            for i in range(0,len(s)):
                if s[i] not in res_set:
                    res_set.add(s[i])
                    result_list.append(s[:i+1])  
                else:
                    passes+=1
                    index_dict[passes]=i
                    # Compare the previous substrings with the current one 
                    if passes>1:
                        result_list.append(s[index_dict[passes-1]:i])
                    else:
                        result_list.append(s[:i])  
            
            print(result_list)
            res = [len(x) for x in result_list]
            print(res)
            return max(res)
