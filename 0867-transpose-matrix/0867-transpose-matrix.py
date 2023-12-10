class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        answer = [[ '' for j in range(len(matrix))] for i in range(len(matrix[0]))]
        # print(answer)
        for i in range(len(matrix)):
            # answer = matrix[i][0]
            for j in range(len(matrix[0])):
                # print(i,j, matrix[i][j])
                answer[j][i] = matrix[i][j]
        return answer
            
        