def q1():
    N = 1260
    count = 0
    for c in [500, 100, 50, 10]:
        count += N // c
        N %= c
    print(count)


def q2():
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    m2, m1 = sorted(lst)[-2:]

    result = 0

    if m1 != m2:
        w2 = M % K
        w1 = M - w2
        result = w1 * m1 + w2 * m2
    else:
        result = M * m1
    
    print(result)


if __name__ == '__main__':
    q1()
    q2()