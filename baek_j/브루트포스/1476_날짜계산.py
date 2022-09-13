E, S, M = map(int,input().split())
num = 1
while True:
    if num % 15 != 0 and num % 28 != 0 and num % 19 != 0:
        if num - (num // 15)*15 == E and num - (num//28)*28 == S and num - (num//19)*19 == M:
            print(num)
            break
    elif num % 15 == 0 and num % 28 == 0 and num % 19 == 0:
        if num - (num // 15 - 1) * 15 == E and num - (num // 28 - 1) * 28 == S and num - (num // 19 - 1) * 19 == M:
            print(num)
            break
    elif num % 15 == 0 and num % 28 == 0:
        if num - (num // 15 - 1) * 15 == E and num - (num // 28 - 1) * 28 == S and num - (num // 19) * 19 == M:
            print(num)
            break
    elif num % 15 == 0 and num % 19 == 0:
        if num - (num // 15- 1) * 15 == E and num - (num // 28) * 28 == S and num - (num // 19 - 1) * 19 == M:
            print(num)
            break
    elif num % 19 == 0 and num % 28 == 0:
        if num - (num // 15) * 15 == E and num - (num // 28 - 1) * 28 == S and num - (num // 19 - 1) * 19 == M:
            print(num)
            break
    elif num % 15 == 0:
        if num - (num // 15 - 1) * 15 == E and num - (num // 28) * 28 == S and num - (num // 19) * 19 == M:
            print(num)
            break
    elif num % 28 == 0:
        if num - (num // 15) * 15 == E and num - (num // 28 - 1) * 28 == S and num - (num // 19) * 19 == M:
            print(num)
            break
    elif num % 19 == 0:
        if num - (num // 15) * 15 == E and num - (num // 28) * 28 == S and num - (num // 19- 1) * 19 == M:
            print(num)
            break


    num += 1