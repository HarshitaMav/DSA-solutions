# We use 2D stack here to keep count and track characters
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1 #if stack not empty and top element matches the char we increment
                if stack[-1][1] == k:
                    stack.pop() # pop if k limit is reached
            else:
                stack.append([char,1])
            
        return ''.join(char*count for char,count in stack) # We multiply each character by its count and join them to form the final string