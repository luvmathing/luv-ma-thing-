import random
num = random.randrange(1,101)
game = True

while game:
    user_num = int(input("숫자를 입력하세요: "))
    if num > user_num:
        print("입력한 값이 제가 생각한 값보다 작습니다.")
    elif num < user_num:
        print("입력한 값이 제가 생각한 값보다 큽니다.")
    else:
        print("정답입니다.")
        break