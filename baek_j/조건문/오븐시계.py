# 오븐시계

H, M = map(int,input().split())
C = int(input())

if M + C < 60:
    print(f'{H} {M + C}')
    
elif H + (M + C)//60 >= 48:
    print(f'{H + (M + C) // 60 - 48} {(M + C) % 60}')

elif (H + (M + C)//60) >= 24:
    print(f'{H + (M + C)//60 - 24} {(M + C) % 60}')

else:
        print(f'{H + (M + C)//60} {(M + C) % 60}')
