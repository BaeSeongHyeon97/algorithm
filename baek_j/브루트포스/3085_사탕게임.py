import copy
N = int(input())
arr = [list(input()) for _ in range(N)]
# 행 검사 상 하
dr1 = [-1, 1]
dc1 = [0, 0]

# 열검사 좌 우
dr2 = [0, 0]
dc2 = [-1, 1]

# 하나 바꾸고 순회 / 하나 바꾸고 전체 순회 반복?
# 바꿀거부터 고르고 진행하기
differnt = []
for r in range(N):
    for c in range(N-1):
        if arr[r][c] != arr[r][c+1]:
            differnt.append((r, c, r, c+1))
for c in range(N):
    for r in range(N-1):
        if arr[r][c] != arr[r][c+1]:
            differnt.append((r, c, r, c+1))




# # 행 순회
# max_cnt = 0
# for r in range(N):
#     cnt = 1
#     arr = copy.deepcopy(origin)
#     for c in range(N-1):
#         if arr[r][c] == arr[r][c+1]:
#             cnt += 1
#         else:  # 다르면 상, 하 검사
#             for i in range(2):
#                 nr = r + dr1[i]
#                 nc = c+1 + dc1[i]
#                 if 0 <= nr < N and 0 <= nc < N:
#                     if arr[nr][nc] == arr[r][c]:
#                         arr[r][c+1] = arr[nr][nc]
#                         cnt += 1
#                         break
#             else:
#                 cnt = 1
#         if cnt == N:
#             max_cnt = N
#             break
#         elif cnt > max_cnt:
#             max_cnt = cnt
#
# # 열 순회
#
# for c in range(N):
#     cnt = 1
#     arr = copy.deepcopy(origin)
#     for r in range(N-1):
#         if arr[r][c] == arr[r+1][c]:
#             cnt += 1
#         else:  # 다르면 상, 하 검사
#             for i in range(2):
#                 nr = r+1 + dr2[i]
#                 nc = c + dc2[i]
#                 if 0 <= nr < N and 0 <= nc < N:
#                     if arr[nr][nc] == arr[r][c]:
#                         arr[r+1][c] = arr[nr][nc]
#                         cnt += 1
#                         break
#             else:
#                 cnt = 1
#         if cnt == N:
#             max_cnt = N
#             break
#         elif cnt > max_cnt:
#             max_cnt = cnt
#
# print(max_cnt)
