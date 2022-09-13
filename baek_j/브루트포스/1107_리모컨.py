# N = input()
# M = int(input())
# buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# if M != 0:
#     breakdown = list(map(int, input().split()))
#     for button in breakdown:
#         if button in breakdown:
#             buttons.remove(button)
# cnt = 0
# ans1 = ''
# ans2 = ''
# # 첫글자는 차이가 가장 작은 것으로 설정하기
# if int(N[0]) in buttons:
#     cnt += 1
#     ans1 += N[0]
#     ans2 += N[0]
#
# else:
#     cnt += 1
#     min_idx1 = 0
#     for i in range(len(buttons)):
#         if abs(int(N[0]) - buttons[i]) < abs(int(N[0]) - buttons[min_idx1]):
#             min_idx1 = i
#     ans1 += str(buttons[min_idx1])
#     ans2 += str(buttons[min_idx1])
#
# # 두번째부터는 차이가 적은것으로 하나, 가장 큰수로 하나해서 크기 비교
# for j in range(1, len(N)):
#     cnt += 1
#     min_idx2 = 0
#     for i in range(len(buttons)):
#         if abs(int(N[j]) - buttons[i]) < abs(int(N[j]) - buttons[min_idx2]):
#             min_idx2 = i
#     ans1 += str(buttons[min_idx2])
#     ans2 += str(max(buttons))
#
# if N == '100':
#     cnt = 0
#     ans1 = 100
#     ans2 = 100
#     exit()
# print(min(cnt + min(abs(int(N) - int(ans1)), abs(int(N) - int(ans2))), abs(int(N) - 100)))

# 위에는 일부만 돌리고 9999 일때 10000으로 가지 못함
# 전수조사를 통해서 풀기
def remote(C):
    cnt = 0
    if C == 0:
        if C in breakdown:
            return False
        else:
            return True

    while C > 0:
        if C % 10 in breakdown:
            return False
        C = C // 10
        cnt += 1  # 버튼을 누른 횟수
    return cnt


N = input()
M = int(input())
buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if M != 0:
    breakdown = list(map(int, input().split()))
else:
    breakdown = []
min_v = 999999999999
if N == '100':
    print(0)
    exit()

for i in range(1000000):
    C = i
    if remote(C):
        val = remote(C) + abs(C - int(N))
        if val < min_v:
            min_v = val
    else:
        val = abs(100 - int(N))
        if val < min_v:
            min_v = val
    if min_v > abs(100 - int(N)):
        min_v = abs(100 - int(N))
print(min_v)