class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openBraces = ['(','[', '{']
        closingBraces = [')', ']', '}']
        stack = []
        for brace in s:
            if brace in openBraces:
                stack.append(brace)
            else:
                if len(stack) != 0:
                    top = stack.pop()
                    if brace != closingBraces[openBraces.index(top)]:
                        return False
                else:
                    return False
        if len(stack) != 0:
            return False
        return True

class Solution1(object):
    def isValid(self, s):
        tempDict = {']':'[', ')':'(', '}':'{'}
        stack = []
        for i in s:
            if i in tempDict.keys() and stack:
                if tempDict[i] != stack.pop():
                    return False
            else:
                stack.append(i)
        
        return False if stack else True


s = Solution1()
print(s.isValid(")  ()("))