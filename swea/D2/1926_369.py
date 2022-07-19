# 간단한 369

'''
1부터 말하되 3,6,9가 있는 수는 말하지 않는다
3,6,9는 들어간 개수만큼 박수
박수는 '-' 로 출력
박수 두번은 '--'/ not '- -' 
'''

N = int(input())

N_li = list(range(1, N + 1))

cout_3 = []
cout_6 = []
cout_9 = []
for i in range(N):
    cout_3.append(str(N_li[i]).count('3'))
    cout_6.append(str(N_li[i]).count('6'))
    cout_9.append(str(N_li[i]).count('9'))

total = []
for j in range(N):
    total.append(int(cout_3[j]) + int(cout_6[j]) + int(cout_9[j]))

for k in range(N):
    if total[k] == 0:
        total[k] = N_li[k]
    elif total[k] == 1:
        total[k] = '-'
    elif total[k] == 2:
        total[k] = '--'
    elif total[k] == 3:
        total[k] = '---'

   
print(*total)