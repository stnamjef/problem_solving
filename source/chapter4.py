def q1():
    N = int(input())
    route = list(input().split())
    
    x, y = 1, 1
    for r in route:
        nx, ny = x, y
        
        if r == 'L':
            ny -= 1
        elif r == 'R':
            ny += 1
        elif r == 'U':
            nx -= 1
        else:
            nx += 1
        
        if nx > 0 and nx <= N and ny > 0 and ny <= N:
            x, y = nx, ny
    
    print(x, y)


def q2():
    N = int(input())

    count = 0
    for i in range(N + 1):
        for j in range(60):
            for k in range(60):
                time = f'{i}{j}{k}'
                if time.find('3') != -1:
                    count += 1
    
    print(count)


def q3():
    loc = input()
    x, y = list(loc)

    x = 'abcdefgh'.find(x) + 1
    y = int(y)

    dxs = [2, -2, 1, -1]
    dys = [2, -2, 1, -1]

    count = 0
    for dx in dxs:
        for dy in dys:
            if abs(dx) + abs(dy) == 3:
                nx, ny = x + dx, y + dy
                if nx > 0 and nx <= 8 and ny > 0 and ny <= 8:
                    count += 1
    
    print(count)


if __name__ == '__main__':
    # q1()
    # q2()
    q3()