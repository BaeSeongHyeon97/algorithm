import sys

N = int(sys.stdin.readline())
Q = [0] * 10000
s, e = -1, -1
for n in range(N):
    command = list(sys.stdin.readline().rstrip().split())
    if command[0] == 'push':
        s += 1
        Q[s] = int(command[1])
    elif command[0] == 'pop':
        if e >= s:
            print(-1)
        else:
            e += 1
            print(Q[e])
    elif command[0] == 'front':
        if s <= e:
            print(-1)
        else:
            print(Q[e+1])
    elif command[0] == 'back':
        if s <= e :
            print(-1)
        else:
            print(Q[s])
    elif command[0] == 'empty':
        if s <= e:
            print(1)
        else:
            print(0)
    elif command[0] == 'size':
        if s <= e:
            print(0)
        else:
            print(s - e)
