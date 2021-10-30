id = "ilovepython"
pw = "123456"
s = input("아이디를 입력하시오: ")
if s == id:
    p = input("패스워드를 입력하시오: ")
    if p == pw:
        print("환영합니다.")
    else:
        print("비밀번호가 잘못되었습니다.")
        
else:
    print("아이디를 찾을 수 없습니다.")