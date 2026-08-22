class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
                
            else:

                if not stack:
                    return False

                popped = stack.pop()

                if (popped == "(" and ch == ")" 
                or popped == "[" and ch == "]" 
                or popped == "{" and ch == "}"):
                    continue
                else:
                    return False

        if not stack:
            return True
        return False

