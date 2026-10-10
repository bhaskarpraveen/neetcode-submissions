class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0 
        end = len(s) - 1
        flag = True
        while(start<end):

            if not ((s[start] >= 'a' and s[start] <= 'z' ) or (s[start] >= 'A' and s[start] <= 'Z') or (s[start] >= '0' and s[start] <= '9')):
                # print(s[start])
                start = start + 1
                continue
            if not ((s[end] >= 'a' and s[end] <= 'z') or (s[end] >= 'A' and s[end] <= 'Z') or (s[end] >= '0' and s[end] <= '9') ):
                end = end - 1
                continue
            # print('-',s[start],s[end])
            if start>=end:
                break
            if s[start].lower() != s[end].lower():
                print(s[start],s[end])
                flag = False
                break
            start = start + 1
            end = end - 1
        return flag
        