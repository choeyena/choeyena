import random

solution = random.randint(0, 99)

user = int(input("복권번호를 입력하시요(0에서 99사이): "))

digit1 = solution // 10
digit2 = solution % 10

u_digit1 = user // 10
u_digit2 = user % 10

print("당첨번호는", solution, "입니다.")

if (digit1 == u_digit1 and digit2 == u_digit2):
    print("상금은 100만원입니다.")
elif (digit1 == u_digit1
        or digit1 == u_digit2
        or digit2 == u_digit1
        or digit2 == u_digit2):
    print("상금은 50만원입니다.")
else:
    print("상금은 없습니다.")