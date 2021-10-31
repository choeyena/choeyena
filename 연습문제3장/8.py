mass = float(input("물체의 무게를 입력하시오(킬로그램): "))
velocity = float(input("물체의 속도를 입력하시오(미터/초): "))

energy = 0.5 * mass * velocity **2
print("물체는 " + str(energy) + " (줄)의 에너지를 가지고 있다.")