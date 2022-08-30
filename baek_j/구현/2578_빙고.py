
def check1():
    global ans
    for a in range(5):
        for b in range(5):
            if arr[a][b] != 0:
                break
        else:
            ans += 1
            return
    return

def check2():
    global ans
    for a in range(5):
        for b in range(5):
            if arr[b][a] != 0:
                break
        else:
            ans += 1
            return
    return

def check3():
    global ans
    for a in range(5):
        if arr[a][a] != 0:
            return
    else:
        ans += 1
        return

def check4():
    global ans
    for a in range(5):
        if arr[a][4 - a] != 0:
            return
    else:
        ans += 1
        return

arr = [list(map(int,input().split())) for _ in range(5)]
call = []
for _ in range(5):
    for i in list(map(int,input().split())):
        call.append(i)
r, c, i = 0, 0, 0
cnt = 0
ans = 0
while ans < 3:
    ans = 0
    if arr[r][c] == call[i]:
        arr[r][c] = 0
        i += 1
        r, c = 0, 0
        check1()
        check2()
        check3()
        check4()
    else:
        c += 1
        if c == 5:
            r += 1
            c = 0


print(i)

