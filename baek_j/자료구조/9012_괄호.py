import sys; input = sys.stdin.readline

T = int(input())
stack = [''] * 50

for _ in range(T):
    top = -1
    string = input().rstrip()
    for s in string:
        if s == '(':
            top += 1
            stack[top] = s
        else:
            if top >= 0:
                top -= 1
            else:
                print('NO')
                break
    else:
        if top >= 0:
            print('NO')
        else:
            print('YES')
