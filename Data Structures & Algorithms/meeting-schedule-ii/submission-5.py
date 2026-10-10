"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals = sorted([(i.end,i.start) for i in intervals], key =lambda x:x[1])

        heap = [intervals[0]]
        for interval in intervals[1:]:
            least = heap[0]
            if (least==interval) or (least[1]<interval[1] and least[0]>interval[1]) or (least[1]<interval[0] and least[0]>interval[0]):
                heapq.heappush(heap,interval)   
            else:
                heapq.heappush(heap,interval)
                heapq.heappop(heap)
        return len(heap)

            



                



