### This (my) version passes only 8 test cases of the several. Do not use
class Solution:
    
    def check_consecutive(self,ind,a,b):
        """
        :param ind: Index of the element which is being compared with index+1
        :param a : List[i] for comparsion
        :param b : List[i+1] for comparsion
        :returns the index and the merged list 
        """
        combined_list=[]
        combined_list.append(ind)
        print("hello")
        last_num_a = a[-1]
        first_num_b = b[0]
        diff = last_num_a-first_num_b
        combined_list.append(a[0])
        combined_list.append(b[-1])
        if abs(diff)<=2:
            return combined_list
        else:
            return False
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        :param list of lists as input
        :returns resultant merged list
        """
        if len(intervals)==1:
            return intervals
        result_list=[]
        for each_list in range(0,len(intervals)-1):
            if each_list!=len(intervals):
                # print(each_list)
                r1 = self.check_consecutive(each_list,intervals[each_list],intervals[each_list+1])
                # print("im",r1)                           
                if r1!=False:
                    print(r1)
                    result_list.insert(r1[0],r1[1:])
                    """
                    print("intervals i",intervals[each_list][:-1])
                    print("intervals i+1", intervals[each_list+1][1:])
                    print(result_list)
                    """
                else:
                    result_list.append(intervals[each_list+1])
            else:
                pass
                    
        #print(result_list)
        return result_list
            
