class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        max_heap = [[-count,char] for char,count in c.items()]
        heapq.heapify(max_heap)
        res = ""
        prev= None
        count = 0
        while max_heap or prev:
            
            if prev and not max_heap:
                return ""
            top = heapq.heappop(max_heap)
            res+= top[1]
            top[0]+=1
            if prev:
                heapq.heappush(max_heap,prev)
                prev = None
            if top[0]!=0:
                prev = top
        return res

            
            




        