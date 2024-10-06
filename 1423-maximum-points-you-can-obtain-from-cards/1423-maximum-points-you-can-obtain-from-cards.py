class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        front_dp = [0] * (k+1)
        end_dp = [0] * (k+1)
        for i in range(1, k+1):
            front_dp[i] = front_dp[i-1] + cardPoints[i-1]
            end_dp[i] = end_dp[i-1] + cardPoints[-i]
        # print(front_dp, end_dp)
        score = 0
        for i in range(k+1):
            # print(i, k-i)
            cur_score = front_dp[i] + end_dp[k-i]
            score = max(score, cur_score)
            # print(score)
        return score
            
        
        