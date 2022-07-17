# 2056. 연월일 달력

T = int(input())

for t in range(1, T+1):
    num = str(input())
    calendar = f'{num[0:4]}/{num[4:6]}/{num[6:]}'
    month = int(calendar[5:7])
    day = int(calendar[8:])
    if month > 13 :
        print(f'#{t} -1')
    elif month < 1 :
        print(f'#{t} -1')
    elif month == 2:
        if day > 28 :
            print(f'#{t} -1')
        else :
            print(f'#{t} {calendar}')
    elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12 :
        if day > 31 : 
            print(f'#{t} -1')
        else :
            print(f'#{t} {calendar}')
    elif month == 4 or 6 or 9 or 11:
        if day > 30 : 
            print(f'#{t} -1')
        else :
            print(f'#{t} {calendar}')