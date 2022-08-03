# 81 16진수 구구단
# 16진수 
n = input()

i = 1
for i in range(17):
   print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

# 16진수... 모르겠다..

n=input()
n=int(n,16)
for i in range(1,16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')