def q1():
    N = list(input())
    N = [int(x) for x in N]

    mid = len(N) // 2

    if sum(N[:mid]) == sum(N[mid:]):
        print('LUCKY')
    else:
        print('READY')


def q2():
    S = list(input())

    num = 0
    strs = []
    for s in S:
        if s.isnumeric():
            num += int(s)
        else:
            strs.append(s)
    
    strs = sorted(strs)
    
    print(''.join(strs) + str(num))


if __name__ == '__main__':
    # q1()
    q2()