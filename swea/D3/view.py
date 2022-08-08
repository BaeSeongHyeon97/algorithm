for n in range(10):
    T = int(input())
    arr = list(map(int,input().split()))
    view = 0
    for i in range(2,T-2):
        first = 0
        second = 0
        for j in arr[i-2:i+3]:
            if j > first:
                second = first
                first = j
            elif j > second:
                second = j
        if first == arr[i]:
            view += first - second
    print(f'#{n+1} {view}')
    