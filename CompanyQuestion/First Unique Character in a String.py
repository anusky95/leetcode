class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :param s: string
        :return ind: integer
        
        1) unique character 
        
        2) return -1 if it does not exist
        
        valid
        "leetcode" -> 0
        "loveleetcode" -> 2
        "hulhef"
        "h" -> 0
        
        invalid
        "" -> -1
        " " -> -1
        
        Algorithm:
        Store each letter in dictionary according to the index for position
        In another dictionary increase count if already present
        traverse the loop and check which key has only one repition
        O(N)
        
        posdict={}
        dicts={}

        if len(s)==0:
            return -1
        if len(s)==1:
            return 0
        for ind,i in enumerate(s):
            if i in posdict:
                continue
            posdict[i]=ind
        
                
        for j in s:
            if j in dicts:
                dicts[j]+=1
            else:
                dicts[j]=1
        print(dicts)
        
        for k,v in dicts.items():
            if v==1:
                return posdict.get(k)
        return -1
        """
        
        """
        Easy elegant solution
        in a dictionary with enumerate check the count of the character
        return the character with one count
        """
        for ind,i in enumerate(s):
            if s.count(i)==1:
                return ind
        return -1
                    
                  
