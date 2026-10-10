class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        s = 0
        if len(prices)==1:
            return 0
        while(l<r and l<len(prices) and r<len(prices)):
            prof = prices[r]-prices[l]
            # print(l,r,prof)
            if(prof>s):
                s = prof
            else:
                if prices[l]>prices[r]:
                    l = r
                    r = r+1
                else:
                    r = r+1
        return s

