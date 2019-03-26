class Solution:
    def isPalindrome(self, s: str) -> bool:

        """
        :input type: string
        :return type: Boolean

        """   
        slist = []
        cleaned_str = ''.join([i for i in s if i.isalnum()])
        cleaned_str = cleaned_str.lower()
        slist = cleaned_str
        
         
    #Method 1 to find if it is a palindrome or not
    #Clean the string, copy it to the list and check if the reverse of the string matches the original 
    #Complexity is O(2N) as copying the string to list takes N time and reversing takes another N time
        
        
        if slist==slist[::-1]:
            return True
        else:
            return False
    
#     #Method 2 to find if it is a palindrome or not
#     #Clean the string, iterate half the string from front and the end and check if its equal, return False if it is not
#      #Complexity is O(N+N/2) as copying the string to list takes N time and reversing takes another N/2 time
     
#     for i in range(int(len(slist)/2)):
#                     if slist[i] != slist[-(i+1)]:
#                         return False
#             return True

      
