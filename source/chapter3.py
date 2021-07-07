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


def q3():
    N, M = map(int, input().split())
    
    max_val = 0
    for i in range(N):
        row = list(map(int, input().split()))
        min_row = min(row)
        if max_val < min_row:
            max_val = min_row
    
    print(max_val)


def q4():
    N, K = map(int, input().split())
    
    count = 0
    while N % K != 0:
        N -= 1
        count += 1
    
    while N // K != 0:
        N //= K
        count += 1
    
    print(count)

if __name__ == '__main__':
    # q1()
    # q2()
    # q3()
    q4()