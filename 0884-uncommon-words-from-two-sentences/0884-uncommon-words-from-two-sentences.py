class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(' ')
        s2 = s2.split(' ')
        unique_s1 = []
        unique_s2 = []
        remove_list = []
        
        for i, s in enumerate(s1):
            s1_temp = s1[:i] + s1[i+1:]
            if not(s in s1_temp):
                unique_s1.append(s)
            elif not (s in remove_list):
                remove_list.append(s)
        for i, s in enumerate(s2):
            s2_temp = s2[:i] + s2[i+1:]
            if not(s in s2_temp):
                unique_s2.append(s)      
            elif not (s in remove_list):
                remove_list.append(s)
                
        print(unique_s1, unique_s2)
        
        for s in unique_s1:
            if s in unique_s2:
                if not (s in remove_list):
                    remove_list.append(s)                
                    
        print(remove_list)
        
        for i in remove_list:
            if i in unique_s1: unique_s1.remove(i)
            if i in unique_s2: unique_s2.remove(i)
        res = set(unique_s1+unique_s2)
        return list(res)