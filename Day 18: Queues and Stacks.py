import sys
class Solution(object):
    def __init__(self):
        self.__stack = []
        self.__queue = []

    def pushCharacter(self, ch):
        self.__stack.append(ch)

    def enqueueCharacter(self, ch):
        self.__queue.insert(0, ch)

    def popCharacter(self):
        return self.__stack.pop()

    def dequeueCharacter(self):
        return self.__queue.pop()
s=raw_input()
obj=Solution()   
l=len(s)
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])   
isPalindrome=True
for i in range(l / 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
if isPalindrome:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")    
    
        
