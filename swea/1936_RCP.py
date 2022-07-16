# 1936. 가위바위보
# 비기는 것 없이
# 가위 1, 바위 2, 보 3

a, b = map(int,input().split())


if a == 1:
    if b == 2:
        print('B')
    elif b == 3:
        print('A')

if a == 2:
    if b == 1:
        print('A')
    elif b == 3:
        print('B')

if a == 3:
    if b == 1:
        print('B')
    elif b == 2:
        print('A')