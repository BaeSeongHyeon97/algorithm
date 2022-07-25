# 윤년
# 윤년이면 1 아니면 0
# 4의 배수이면서, 100의 배수가 아닐때 또는 400의 배수일때

year = int(input())

if year % 4 != 0:
    print(0)
elif year% 100 != 0:
    print(1)
elif year % 400 != 0:
    print(0)
else:
    print(1)