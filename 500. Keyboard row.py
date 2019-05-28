class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        """
        Declare three strings with same characters as keyboard
        Check which row each letter in the words belong to and append to new list as first row, second row or third row of keyboard.
        Check the latest list created to see which one has all same rows and output them
        """
        
        
        frow = "qwertyuiop{[\|]}"
        srow = "asdfghjkl;:'""'"
        trow = "zxcvbnm,<.>/?"
        mainlist=[]
        output=[]
        word_num=0
        for i in words:
            rowlist=[]
            i = i.lower()
            for j in i:
                if frow.find(j)!=-1:
                    rowlist.append("frow")
                elif srow.find(j)!=-1:
                    rowlist.append("srow")
                else:
                    rowlist.append("trow")
            mainlist.append(rowlist)
        for i in mainlist:
            word_num=word_num+ 1
            if all(x == i[0] for x in i):
                output.append(words[word_num-1])
        return output
    
    
    """
    Time Complexity:
    O(2*n^2) = O(n^2) : O(n^2) for the first part for finding row and appending
                        O(n^2) for the second part for checking if same rows & append to output
                            
    """
