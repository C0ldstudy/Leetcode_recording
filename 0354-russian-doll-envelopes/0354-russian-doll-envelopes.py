class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        sorted_env = [i[1] for i in envelopes]
        
        sub = []
        for ei in range(len(sorted_env)):
            idx = bisect_left(sub, sorted_env[ei])
            if idx == len(sub):
                sub.append(sorted_env[ei])
            else:
                sub[idx] = sorted_env[ei]
        return len(sub)
                        
                
        
        
        