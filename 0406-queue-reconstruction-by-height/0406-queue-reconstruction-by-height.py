class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        for p in people:
            queue.insert(p[1], p)
        return queue
                        
            
        