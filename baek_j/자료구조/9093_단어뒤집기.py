import sys;

T = int(sys.stdin.readline())
stack = [0] * 20000
for _ in range(T):
    top = -1
    ans = ''
    words = list(input())
    N = len(words)
    for word in words:
        if word != ' ':
            top += 1
            stack[top] = word
        else:
            while top >= 0:
                ans += stack[top]
                top -= 1
            ans += word
    while top >= 0:
        ans += stack[top]
        top -= 1
    print(ans)
