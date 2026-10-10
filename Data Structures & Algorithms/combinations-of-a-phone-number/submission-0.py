class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res = []
        
        def backTracking(i,string):
            if len(string) == len(digits):
                res.append(string)
                return
            
            for c in dic[digits[i]]:
                backTracking(i+1,string + c)
        if digits:
            backTracking(0,"")
        return res
