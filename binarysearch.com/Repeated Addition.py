# https://binarysearch.com/problems/Repeated-Addition
def solves(num):
    while num > 9:
        s = 0
        while num > 0:
            s += num % 10
            num //= 10
        return s


n = int(input('Num: '))

print(solves(n))
