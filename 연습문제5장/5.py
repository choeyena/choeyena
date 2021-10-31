import random
x = random.randint(1, 100)
y = random.randint(1, 100)

ans = int(input(str(x)+"-"+str(y)+"="))

if ans == x - y :
    print("맞았습니다.")
else :
    print("틀렸습니다.")