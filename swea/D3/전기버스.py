# A도시는 전기버스를 운행 한번 충전으로 이동할 수 있는 정류장 수가 정해져있음
# 충전기가 설치된 정류장 있음
# 0번에서 출발해 종점 N번 최대이동 K정류장
# 충전기가 설치된 M개의 정류장 번호, 최소한 몇번의 충전을 해야 종점 도착?
# 충전기 설치 잘못되어 종점 도착 못하는 경우 0
# 출발지 포함 x

import sys; sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int,input().split())
    bus_stations = list(map(int,input().split()))
    c = [0] * (N + 1)

    for i in range(M):
        c[bus_stations[i]] += 1

    for j in range(M-1):
        if bus_stations[j + 1] - bus_stations[j] > K or bus_stations[0] > K:
            cnt = 0
            break

    else:
        idx = 0
        cnt = 0
        k = K
        while idx + k < N:
            if c[idx+k] == 1:
                idx = idx + k
                cnt += 1
                k = K
            else:
                k -= 1

    print(f'#{tc} {cnt}')