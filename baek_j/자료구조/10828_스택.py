import sys

N = int(sys.stdin.readline())
stack = [0] * 10001
top = -1
for _ in range(N):
    command = list(sys.stdin.readline().split())
    # push 나오면 top += 1후 스택에 추가
    if command[0] == 'push':
        top += 1
        stack[top] = int(command[1])

    # top 나오면 top출력
    elif command[0] == 'top':
        if top < 0:
            print(-1)
        else:
            print(stack[top])

    # size나오면 스택에 있는 정수의 개수
    elif command[0] == 'size':
        if top < 0:
            print(0)
        else:
            print(top + 1)

    # empty나오면 비어있는지 확인
    elif command[0] == 'empty':
        if top < 0:
            print(1)
        else:
            print(0)
    # pop 나오면 정수 프린트 후 top -= 1
    elif command[0] == 'pop':
        if top < 0:
            print(-1)
        else:
            print(stack[top])
            top -= 1


