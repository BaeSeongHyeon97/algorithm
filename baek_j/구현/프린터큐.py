T = int(input())
for tc in range(T):
    N, M = map(int,input().split())  # N은 문서의 개수, M은 몇번째로 인쇄된지 궁금한 문서의 현재 위치
    arr = list(map(int,input().split()))   # 리스트 받기 / 각 값은 중요도를 의미함
    ans = 1
    # 튜플로 원래 index와 묶어버리기
    for i in range(N):
        arr[i] = (arr[i], i)

    # 뒤에 큰게 있다면 맨 뒤로 보내기
    a = 0
    while a < N:
        for j in range(a, N):
            if arr[a][0] < arr[j][0]:   # 뒤에꺼에서 작은게 있다면
                arr.append(arr.pop(a))  # 뒤로 보내기
                break
        else:  # 만약 뒤에 큰게 없다면 앞자리를 바꾼다
            a += 1

    for k in range(N):
        if arr[k][1] != M:
            ans += 1
        else:
            break

    print(ans)

    

