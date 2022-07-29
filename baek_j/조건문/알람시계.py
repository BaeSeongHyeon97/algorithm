# 알람시계
# 45분일찍 알람설정

H, M = map(int,input().split())
alarm_H = 0
alarm_M = 0

if M >= 45:
    alarm_H = H
    alarm_M = M - 45
elif 0 <= M < 45:
    if H == 0:
        alarm_H = H + 23
        alarm_M = M + 15
    else:
        alarm_H = H - 1
        alarm_M = M + 15



print(alarm_H, alarm_M)
