N = int(input())
scores = list(map(int,input().split()))
max_score = max(scores)

result=[]
for score in scores:
    result.append(score / max_score * 100)

print(sum(result)/len(result))

