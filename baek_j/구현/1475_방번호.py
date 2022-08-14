num = int(input())
# 0 ~ 9의 한세트의 리스트 만들어놓기
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cnt = 1
# 받은 숫자에서 한세트 리스트에 있는지
# 6, 9 는 바꿔서 쓸수 있음 => 두개 씩 가능 나머지는 하나만
while num > 0:
    if num % 10 in nums:   # 1의자리 숫자가 리스트에 있으면 그 숫자 지우기
        nums.remove(num % 10)
    elif num % 10 == 6 and (9 in nums):  # 6이 리스트에 없는데 9가 있다면
        nums.remove(9)                   # 9를 지우기
    elif num % 10 == 9 and (6 in nums):  # 9가 리스트에 없는데 6이 있다면
        nums.remove(6)                   # 6을 지우기
    else:  # 리스트에 1의 자리 숫자가 없다면
        cnt += 1  # 새로운 세트를 까고
        nums += [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 새로운 세트 추가
        continue
    num //= 10

print(cnt)

