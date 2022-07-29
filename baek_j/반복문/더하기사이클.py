N = int(input())
original = N
cout = 0

while True:
    if N < 10:
        N = '0'+ str(N)
    else:
        N = str(N)
    if len(str(int(N[0]) + int(N[1]))) < 2:
        N = int(N[1] + str(int(N[0]) + int(N[1])))
    else:
        N = int(N[1] + str(int(N[0]) + int(N[1]))[1])
    cout += 1
    if N == original:
        break

print(cout)
    