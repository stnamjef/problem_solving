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



def q3():
    S = list(input())
    N = len(S)

    lengths = []
    for n in range(1, N // 2 + 1):
        length = 0
        count, string = 1, S[:n]
        for i in range(n, N - N % n, n):
            if S[i:i + n] == string:
                count += 1
            else:
                length = length + n if count == 1 else length + n + len(str(count))
                count, string = 1, S[i:i + n]
        length = length + n + (N % n) if count == 1 else length + n + len(str(count))
        lengths.append(length)
    
    print(min(lengths))


if __name__ == '__main__':
    # q1()
    # q2()
    q3()