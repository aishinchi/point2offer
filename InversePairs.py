class Solution:
    def InversePairs(self, data):
        # write code here
        lens = len(data)
        if lens == 0 or lens == 1:
            return 0
        count = 0
        for i in range(1, lens):
            j = i - 1
            while data[j] > data[i] and i >= 1:
                temp = data[j]
                data[j] = data[i]
                data[i] = temp
                j -= 1
                i -= 1
                count += 1
        return count % 1000000007

a = Solution()
print(a.InversePairs([1,2,3,4,5,6,7,0]))