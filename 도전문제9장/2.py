items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}

while True:
     print("")
     print("# 재고 목록 #")
     for key in sorted(items.keys()):
         print(key, items[key])
         
     print("\n********************")
     print("0. 종료")
     print("1. 재고 추가")
     print("2. 재고 삭제")
     print("********************\n") 
     a = int(input("무엇을 하시겠습니까?: "))
 
     if a == 1: 
         item = input("물건의 이름을 입력하시오: ")
         num = input("몇개를 추가하시겠습니까? :")
         items[item] = int(items[item]) + int(num)
 
     elif a == 2:
         item = input("물건의 이름을 입력하시오: ")
         num = input("몇개를 삭제하시겠습니까? :")
         items[item] = int(items[item]) - int(num)
 
     else:
         break