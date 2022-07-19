# 2043. 서랍의 비밀번호

'''
비밀번호 P : 000 ~ 999
K부터 1씩 증가
P,K주어질때 몇번만에 P맞추는지
'''

p, k = map(int,input().split())
cout = 1

while True:
    if k == p :
        print(cout)
        break
    else:
        k += 1
        cout += 1
    