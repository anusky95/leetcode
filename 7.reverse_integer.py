class Solution:
    def reverse(self, x: int) -> int:
         
#             listx = [i for i in str(x)]
#             if listx[0].isdigit()==False:
#                 newlistx = listx[1:]
#                 revnum = newlistx[::-1]
#                 revnum.insert(0,listx[0]) 
#             else:
#                 revnum = listx[::-1]

#             finalnum =  int(''.join(revnum))
#             if finalnum.bit_length() > 32:
#                 return 0
#             else:
#                 return finalnum

        # if the integer is less than 0, then add - and return the reversed integer
        rev = int('-' + str(x)[:0:-1]) if x<0 else int(str(x)[::-1])
        
        # if the signed integer overflows (2^31-1) then return 0
        return rev if rev.bit_length()<32 else 0
    
        # Total three test cases
        # 1 - Negative integer 
        # 2 - Positive integer
        # 3 - Signed integer overflow
