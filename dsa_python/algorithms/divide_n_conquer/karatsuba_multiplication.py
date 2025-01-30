import math


def split_num(num, n_by_2):
    str_num = str(num)
    n = len(str_num)
    # print(n)
    p1 = str_num[:n_by_2]
    p2 = str_num[n_by_2:]
    return int(p1), int(p2)


def karatsuba_mul(num1, num2):
    n1 = len(str(num1))
    n2 = len(str(num2))
    # print("n1: {}, n2: {}".format(n1, n2))
    # print(num1, num2)
    n = max(n1, n2)
    if n1 == 1 or n2 == 1:
        return num1 * num2
    if n % 2 == 0:
        # n_by_2 = int(math.floor(n/2))
        n_by_2 = int(n//2)
    else:
        n += 1
        # n_by_2 = int(math.floor(n/2)) - 1
        n_by_2 = int(n//2) - 1
    a, b = split_num(num1, n_by_2)
    c, d = split_num(num2, n_by_2)
    ac = karatsuba_mul(a, c)
    bd = karatsuba_mul(b, d)
    ad_plus_bc = karatsuba_mul(a+b, c+d) - ac - bd
    return 10**(n) * ac + 10**(n_by_2)*ad_plus_bc + bd


def karat(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        m2 = m // 2

        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)

        z0 = karat(b,d)
        z1 = karat((a+b),(c+d))
        z2 = karat(a,c)

        return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)


if __name__ == '__main__':
    # x = 5678
    # y = 1234
    
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627

    # n_by_2 = len(str(x))//2
    # a, b = split_num(x, n_by_2)
    # print(a, b)
    # a, b = split_num(113, n_by_2)
    # print(a, b)

    print(karatsuba_mul(x, y))
    print(karat(x, y))
    print(x * y)
