# 캠핑장은 연속하는 20일 중 10일 만 사용가능
# 28일 휴가를 시작
# 이번휴가 강산이는 캠핑장에 며칠동안 사용가능?
# 캠핑장 P일중, L일 동안만 사용가능/ V일짜리 휴가
# 마지막줄 0 0 0 출력

i = 1
while True:
    camping = 0
    L, P, V = map(int,input().split())
    if L != 0:
        if (V % P) < L:
            camping = (V // P) * L + (V % P)
            print(f'Case {i}: {camping}')
            i += 1
        else:
            camping = (V // P) * L + L
            print(f'Case {i}: {camping}')
            i += 1
    else:
        break