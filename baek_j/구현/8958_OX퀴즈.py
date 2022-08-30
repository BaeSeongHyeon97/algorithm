T = int(input())

for _ in range(T):
    quiz = input()
    score = 0
    ans = 0
    for q in quiz:
        if q == 'O':
            score += 1
            ans = ans + score
        else:
            score = 0
    print(ans)