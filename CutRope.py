#动态规划
class CutRope(object):
    def maxProduct(self, n):
        if n <= 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        product = [0, 1, 2, 3]

        i = 4
        while i <= n:
            max = 0
            for j in range(1,int(i/2+1)):
                product1 = product[j]*product[i-j]
                if max < product1:
                    max = product1
            product.append(max)
            i = i + 1

        return product[i-1]

#贪心算法
class CutRopeGreedy():
    def maxProduct(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        num1 = int(n / 3)

        if n - num1*3 == 1:
            num1 = num1 - 1

        num2 = int((n - num1*3) / 2)

        product = (3**num1) *(2**num2)

        return product

a = CutRope()
print(a.maxProduct(8))

b = CutRopeGreedy()
print(b.maxProduct(8))