def q1():
    N = int(input())
    levels = list(map(int, input().split()))
    levels = sorted(levels, reverse=True)

    n_groups = 0
    for lv in levels:
        N -= lv
        if N < 0:
            break
        n_groups += 1
    
    print(n_groups)


def q2():
    S = [int(s) for s in list(input())]

    total = S[0]
    for i in range(1, len(S)):
        first = total
        second = S[i]
        if first == 0 or first == 1 or second == 0 or second == 1:
            total += second
        else:
            total *= second
    
    print(total)


def q3():
    S = [int(s) for s in list(input())]

    count = 0
    target = 1 if S[0] == 0 else 1
    for i in range(1, len(S)):
        if S[i] == target and S[i + 1] != target:
            count += 1        
    
    print(count)


if __name__ == '__main__':
    # q1()
    # q2()
    q3()