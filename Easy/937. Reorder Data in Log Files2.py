/*

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.


*/


class Solution:  
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

#     1) List of strings
#     2) Firstword - alphanum identifier
#        a) [a-z]+ - letterlogs  
#        b) [0-9]+ - digitlogs
#     3) Reorder
#        letterlogs (alphabetical only words)  digitlogs (original order) 

#        Pseudocode
#        identify the letterlogs using regex
#        identify the digit logs
#        the starting letter of the second word in each letter log and
#        if first1 = first2 compare second1 and second2 and so on

    
        # Two new lists for storing the letter and digit log
        letter_logs=[]
        dig_logs=[]
        
        #Identify the two types of logs and store them separately
        for i in logs:
            if i.split(' ')[1].isdigit()!=True:
                letter_logs.append(i)
                
            else:
                dig_logs.append(i)
                
        # Sort the letter log based on simple sort 
        letter_logs.sort()
        # sort the logs based on the first key as the first word and if both first  words are same 
        # then compare the second words (1:)
        letter_logs.sort(key=lambda n:((n.split(" ")[1]),(n.split(" ")[1:])))
        reslist = letter_logs + dig_logs
                    
        return reslist
