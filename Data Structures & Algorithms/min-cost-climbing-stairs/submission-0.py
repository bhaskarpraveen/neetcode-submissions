class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        minCost = 0

        i = len(cost)
        while i>1:
            if cost[i-1]<cost[i-2]:
                minCost+=cost[i-1]
                i=i- 1
            else:
                minCost+=cost[i-2]
                i= i-2

        return minCost


        