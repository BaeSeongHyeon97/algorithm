# 더하기_4

while True:
    A, B = map(int,input().split())
    if A < 0 or B > 10:
        break
    else:
        print(A + B)