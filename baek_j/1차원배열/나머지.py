
nums = []
for i in range(10):
    n = int(input())
    nums.append(n)

rests = []
for num in nums:
    rests.append(num % 42)

print(len(set(rests)))
