# 주사위 세개

# 1에서 6까지의 눈을 가진 3개의 주사위를 던져서 규칙에 따라 상금
# 같은눈 3개 10,000 + 같은눈 * 1000
# 같은눈 2개 1000 + 같은눈 * 100
# 모두 다른눈 가장 큰눈 * 100'

a, b, c = map(int,input().split())

nums = [a, b, c]
nums.sort()

if a == b == c:
    print(10000 + a * 1000)

elif a == b or b == c or c == a:
    print(1000 + nums[1] * 100)

else:
    print(nums[2] * 100)




