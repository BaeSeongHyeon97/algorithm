# 초심자의 회문검사

T = int(input()) 

for i in range(1, T+1):
    case = list(str(input()))
    case_rev = case[::-1]
    if case == case_rev :
        print(f'#{i} 1')
    else :
        print(f'#{i} 0')

