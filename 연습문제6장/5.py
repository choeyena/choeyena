sum = 0
while True:
    x = int(input("정수를 입력하시오: "))
    if x == 0:
        break;
    sum = sum + x
    
print("합은", sum, "입니다.")