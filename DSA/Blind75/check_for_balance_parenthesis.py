class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return False
        else:
            stack = []
            i = 0
            while i < n:
                if s[i] == "(" or s[i] == "[" or s[i] == "{":
                    stack.append(s[i])
                else:
                    if len(stack) == 0:
                        return False
                    popped = stack.pop()
                    if (s[i] == ")" and popped == "(") or (s[i] == "]" and popped == "[") or (
                            s[i] == "}" and popped == "{"):
                        pass
                    else:
                        return False
                i += 1
            if stack:
                return False
            else:
                return True


