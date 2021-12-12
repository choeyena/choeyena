import pickle
# 게임에서 사용되는 딕셔너리
addressBook = {"names":["김김김","이이이","박박박","홍길동"],
               "mails":["aaa@gmail.com","bbb@gmail.com","ccc@gmail.com","ddd@gmail.com"],"address":["seoul","daejeon","daegu","busan"]}
# 이진 파일 오픈
file = open("save.p","wb")
# 딕셔너리를 피클 파일에 저장
pickle.dump(addressBook,file)
# 파일을 닫는다. file.close()

# 이진 파일 오픈
file = open("save.p","rb")
# 피클 파일에 딕셔너리를 로딩
obj = pickle.load(file)
print(obj)