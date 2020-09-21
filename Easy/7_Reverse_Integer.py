class Solution:
    def reverse(self, x: int) -> int:
        
        if x>=2**31-1 or x<=-2**31 or x==0:
            return 0
        
        else:
            str_x = str(x)
            if x>0:
                
                rev_x = str_x[::-1]
                int_x = int(rev_x)
                resx = int_x
                
            else:
            
                tmp = str_x[1:]
                rev_x = tmp[::-1]
                resx = '-' + rev_x
                
        if int(resx)>=2**31-1 or int(resx)<=-2**31:
            return 0
        else: return int(resx)
            
