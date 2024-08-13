# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenth_dict = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            print(c)
            # if c in parenth_dict:
            #     stack.append(c)
            #     print('c is here.', stack)
            # elif parenth_dict[stack[-1]] == c:
            #     stack.pop()
            #     print('pop out!', stack)
            # else:
            #     print('will return..')
            #     return False

        print(stack)
        return True if len(stack) == 0 else False

# Test
sol = Solution()
print('sol result:', sol.isValid('()'))