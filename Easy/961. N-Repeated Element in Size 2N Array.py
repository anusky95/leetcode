class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        """
        Runtime: 220 ms, faster than 43.90% of Python3 online submissions for N-Repeated Element in Size 2N Array.
        Memory Usage: 15.3 MB, less than 7.52% of Python3 online submissions for N-Repeated Element in Size 2N Array.
        
        Store the value in dictionary and increase its counter every time you see it.
        Return the key of the. vaue which matches len(n)/2
        
        :param A : List of integers
        :returns k : result integer
        """
        
        
        repnum = len(A)/2
        dicts={}
        for i in A:
            if i in dicts:
                dicts[i]+=1
            else:
                dicts[i]=1
        for k,v in dicts.items():
            if v==repnum:
                return k
            
