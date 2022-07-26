# 오븐시계

A, B = map(int,input().split())
C = int(input())

hour = 0
minute = 0

if B + C < 60:
    hour = A
    minute = B + C

elif B + C > 60:
    if A == 23:
        hour = A - 24 + (B+C) // 60
        minute = (B+C) % 60
    elif A + (B + C) // 60 > 24:
        hour = A - 24 + (B+C) // 60
        minute = (B+C) % 60
    else:
        hour = A + (B+C) // 60
        minute = (B+C) % 60
print(hour, minute)
