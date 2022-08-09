T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int,input()))
    # 입력받은 숫자들을 각각 index로 이용해서 카운트

    c = [0] * 10
    for i in range(N):
        c[arr[i]] += 1
    # c의 최대값과 그의 idx를 저장
    max_val = c[0]
    max_idx = 0
    for j in range(10):
        if c[j] >= max_val: # 값이 같은 경우에는 idx가 큰 경우로 설정
            max_val = c[j]
            max_idx = j
    print(f'#{tc + 1} {max_idx} {max_val}')

    #-----------------------------------------------------
    # 인덱스만 사용
    # max_idx = 0
    # for j in range(10):
    #     if c[j] >= c[max_idx]: # 값이 같은 경우에는 idx가 큰 경우로 설정
    #         max_idx = j
    # print(f'#{tc + 1} {max_idx} {c[max_idx]}')

    # 한번만에 최솟값과 등장 횟수
    # 카운트 변수 만들기
    # min_idx = 0
    # cnt = 0
    # for j in range(10):
    #     if c[j] >= c[max_idx]: # 값이 같은 경우에는 idx가 큰 경우로 설정
    #         max_idx = j
    #         cnt = 1
    #     elif c[j] == c[max_idx]:
    #         cnt += 1
