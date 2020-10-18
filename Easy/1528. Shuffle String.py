class Solution:
    
    """
    Submission Stats: 
    Runtime: 52 ms, faster than 83.58% of Python3 online submissions for Shuffle String.
    Memory Usage: 14.1 MB, less than 99.99% of Python3 online submissions for Shuffle String.
    
    
    Explanation:
    1) Store the string and indices in the dictionary - {4:'c',5:'o',6:'d',3:'t'....}
    2) Access each of these keys in increasing order using range function.

    """
    def restoreString(self, s: str, indices: List[int]) -> str:
        alpha_dict = {}
        shuffled_str = ""
        for a,b in zip(list(s),indices):
            alpha_dict[b] = a 
        for i in range(len(indices)):
            shuffled_str+=alpha_dict[i]
            
        return shuffled_str   
        
