# 정수 A를 B로 바꾸려고 한다.
# 2를 곱한다
# 1을 수의 가장 오른쪽에 추가한다.
# A를 B로 바구는데 필요한 연산의 최솟값

A, B = map(int,input().split())
cnt = 0
while True:
    if B < A:
        cnt= -1
        break

    elif B % 10 == 1:
        B = B // 10
        cnt += 1 
        if B == A:
            cnt += 1
            break           
    elif B % 2 == 0:
        B = B // 2
        cnt += 1 
        if B == A:
            cnt += 1
            break

    else:
        cnt = -1
        break
print(cnt)