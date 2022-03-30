import random

number = random.randint(1,9)
print(number)
a = int(input('숫자 입력: '))
b = int(input('숫자 입력: '))
number = a*b

while True:
    guess = int(input('숫자를 입력하세요 :'))
    if guess == number:
        print('정답입니다')
        break
    elif guess != number:
        print('틀렸습니다')
    else:
        user = int(input("멈추시겠습니까?"))
        print("Press Enter")


