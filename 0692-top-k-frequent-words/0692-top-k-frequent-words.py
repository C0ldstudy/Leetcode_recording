class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # use a dictionary to save the words and the frequencies        
        word_dict = {}
        for word in words:
            if not word in word_dict.keys():
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        # reverse to find the words that have the same frequency                
        result_keys = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
        result = []
        frequency_dict = {}
        for i in result_keys:
            if not i[1] in frequency_dict.keys():
                frequency_dict[i[1]] = [i[0]]
            else:
                frequency_dict[i[1]].append(i[0])
        # output the top k
        for i in sorted(frequency_dict.keys(), reverse=True):
            for j in sorted(frequency_dict[i]):
                result.append(j)
                if len(result) == k:
                    return result
        
        return result