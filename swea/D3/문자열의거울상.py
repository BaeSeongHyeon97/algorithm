T = int(input())
for tc in range(1, T + 1):
    string = list(input())
    n = len(string)
    # 순서 뒤집고
    for i in range(n // 2):
        string[i], string[n - 1 - i] = string[n - 1 - i], string[i]
    print(string)
    # b -> d, d -> b, p -> q, q -> p 시행
    for j in range(n):
        if string[j] == 'b':
            string[j] = 'd'
        elif string[j] == 'd':
            string[j] = 'b'
        elif string[j] == 'p':
            string[j] = 'q'
        elif string[j] == 'q':
            string[j] = 'p'

    print(f'#{tc}', end= ' ')
    for k in range(len(string)):
        print(string[k], end='')
    print()



