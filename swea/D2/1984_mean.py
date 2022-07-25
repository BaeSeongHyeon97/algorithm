# 1984 중간 평균값 구하기

T = int(input())

for t in range(1, T+1):
    nums = list(map(int,input().split()))
    max_num = nums[1]
    for idx1 in range(len(nums)):
        if nums[idx1] > max_num:
            max_num = nums[idx1]
        
    min_num = nums[1]
    for idx2 in range(len(nums)):
        if nums[idx2] < min_num:
            min_num = nums[idx2]
    nums.remove(max_num)
    nums.remove(min_num)
    total = 0
    for num in nums:
        total += num
    average = int(round(total / len(nums), 0))

    print(f'#{t} {average}')
