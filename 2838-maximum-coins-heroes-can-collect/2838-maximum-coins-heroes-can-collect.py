class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        coins = [x for _, x in sorted(zip(monsters, coins))]
        monsters.sort()
        # print(coins, monsters)
        idx = [i for i, _ in sorted(enumerate(heroes), key=lambda x: x[1])]
        heroes.sort()
        # print(idx)
        ans = [0] * len(heroes)
        midx = 0
        
        for i in range(0, len(heroes)):
            if midx == len(monsters): 
                ans[idx[i]] += ans[idx[i-1]]
                continue
            while heroes[i] >= monsters[midx]:
                ans[idx[i]] += coins[midx]
                midx += 1
                # print(i, midx, len(monsters))
                
                if midx == len(monsters): 
                    break
                    
            if i != 0: 
                ans[idx[i]] += ans[idx[i-1]]
            
        return ans
        
            
            
        
        

