T = int(input())

for t in range(1, T + 1):
    num1, num2, calc = input().split()
    if calc == '+':
        print(f'#{t} {int(num1) + int(num2)}')
    elif calc == '-':
        print(f'#{t} {int(num1) - int(num2)}')
    elif calc == '*':
        print(f'#{t} {int(num1) * int(num2)}')
    elif calc == '/':
        print(f'#{t} {int(int(num1) / int(num2))}')