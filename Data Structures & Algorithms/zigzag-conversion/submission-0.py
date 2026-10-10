class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows ==1:
            return s
        res = ""
        for r in range(0,numRows):
            cal = (numRows-1) * 2
            i = r
            while i < len(s):
                res+=s[i]

                if r>0 and r<numRows-1 and (cal - (2*r) + i) <len(s):
                    res+=s[cal - (2*r) + i]
                
                i+=cal
        return res
                




        