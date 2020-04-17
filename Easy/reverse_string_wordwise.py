#Reverse a string

#This is Python
#Python is This

"""
:input type str
:rtype str

"""

def revr(str1):
    #Create two empty lists for storing the words
    listres=[]
    reverselist=[]
    
    #Storing each word in the firstlist
    for i in str1.split(' '):
        listres.append(i)
    
    #Accessing the list in the reverse order and storing in second list
    for i in range(len(listres)-1,-1,-1):
        reverselist.append(listres[i])
    return ' '.join(reverselist)
    

    

str1 = "This is Python"
res = revr(str1)
print(res)
