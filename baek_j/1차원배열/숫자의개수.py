# ABC가 주어질 때 A*B*C에 0부터 9까지 각각의 숫자가 몇번씩 쓰였는지.

a = int(input())
b = int(input())
c = int(input())

num = list(str(a * b * c))
li = []
for i in range(0,10):
    li.append([0])

for n in range(0,10):
    li[n] = num.count(str(n))


for j in li:
    print(j)