"""
1652. Defuse the Bomb
Easy

8

7

Add to List

Share
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

 

Example 1:

Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
Example 2:

Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0. 
Example 3:

Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
 

Constraints:

n == code.length
1 <= n <= 100
1 <= code[i] <= 100
-(n - 1) <= k <= n - 1



"""




class Solution:
    def decrypt(self, A: List[int], K: int) -> List[int]:
        """
        k>0 sum next k num
        code = [5,7,1,4], k = 3
        
        1+2+3
        2+3+0
        3+0+1
        
        5 -> 7+1+4 = 12  i+1 i+2 i+3
        7 -> 1+4+5 = 10  i+1 i+2 
        1 -> 4+5+7 = 16
        
        for each number -> find the next k numbers 
        if k>counts:
            code[i%]
        
        k<0 sum previous k num
        k==0 all i = 0
        
        https://leetcode.com/problems/defuse-the-bomb/discuss/935371/Kt-Js-Py3-Cpp-One-Step-at-a-Time
        
        
        """
         
        t = len(A)
        sums=0
        if not K:    # IF K==0
            return [0]*t
        
        db = []
        step = lambda i: i + 1 if i + 1 < t else 0
        if K>0:
            for i in range(t):
                steps=K
                sums=0
                j=step(i)
                while steps:
                    sums+=A[j]
                    j = step(j)
                    steps-=1
                db.append(sums)
        elif K<0:
            return self.decrypt(A[::-1],-K)[::-1]
                    
        return db
        
        """
        Takeaway : Use Lambda functions instead of logic within for loop
        use recursion to the best advantage
        
        
        """
