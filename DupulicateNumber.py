class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        lens = len(numbers)
        if lens == 0:
            return False
        dic = dict()
        for i in range(lens):
            if numbers[i] in dic:
                dic[numbers[i]] += 1
            else:
                dic[numbers[i]] = 1
        for item in dic:
            if dic[item] > 1:
                duplication[0] = item
                return True
        return False


a = Solution()
print(a.duplicate([2,4,3,1,4],[-1]))