class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        # if length of two strings are not equal return false
        if len(A)!=len(B):
            return False
        
        # In case we have strings such as ("ab","ab") or ("aa","aa") check and return True for ("aa","aa")
        if A==B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
        # if there are different letters in the set like ("ab,"ab") then return False
            return False
        
        #For all other cases like ("abcd","badc"), check if only 2 letters are swapped or more
        else:
            pairs=[]
            for a,b in zip(A,B):
                if a!=b:
                    pairs.append((a,b))
                    
        #pairs would contain [(a,b),(b,a),(c,d)] which means more than two sets of letters are swapped return false
                if  len(pairs)>=3:
                    return False
        # pairs which contain just two pairs of letters and which are swapped ([a,b),(b,a)] should return true
            return len(pairs)==2 and pairs[0] == pairs[1][::-1]
