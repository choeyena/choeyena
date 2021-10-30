money = int(input("투입한 돈: "))
price = int(input("물건 값: "))

change = money - price
coin500s = change // 500
change = change % 500
coin100s = change // 100
print("500원 동전의 개수: ", coin500s)
print("100원 동전의 개수: ", coin100s)