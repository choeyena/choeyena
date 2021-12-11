import random
number = random.randint(1,8)

list = ["한 점의 의심도 없이 맞습니다.", "할 수 있습니다.", "물론입니다.", "글쎄요. 열심히 해야 할 것입니다.", "안 될 것 같습니다.", "조금 더 노력하세요.", "행운을 빕니다.", "다음 달에 할 수 있을 겁니다."]

while True:  
    name = input("이름: (종료하려면 엔터키) ")
    if name == '':
        break;
    question = input("무엇에 대하여 알고 싶은가요? ")
    print(name, "님", "\"", question ,"\"에 대하여 질문 주셨군요.")
    print("운명의 주사위를 굴려볼게요...")
    print(list[number-1])