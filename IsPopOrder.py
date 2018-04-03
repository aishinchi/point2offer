class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV and not popV:
            return True
        stack = []
        stack.append(pushV[0])
        pushV.pop(0)  # pop()的参数是索引啊
        while pushV or stack:
            if stack[-1] == popV[0]:
                popV.pop(0)
                stack.pop()
            elif stack[-1] != popV[0]:
                if not pushV:
                    return False
                stack.append(pushV[0])
                pushV.pop(0)
        if not popV:
            return True
        else:
            return False


a = Solution()
print(a.IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))