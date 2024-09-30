class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        env = [e[1] for e in envelopes]
        
        sub = []
        for ei in range(len(env)):
            idx = bisect_left(sub, env[ei])
            if idx == len(sub):
                sub.append(env[ei])
            else:
                sub[idx] = env[ei]
        return len(sub)
        