class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #make key value pairs
        dic = {}
        for i in range(0,len(position)):
            dic[position[i]] = speed[i]
        # Sort array
        position = sorted(position,reverse= True)
        stack = []

        for i in position:
            stack.append(((target-i)/dic[i]))
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)


        
        
        