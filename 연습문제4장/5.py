str=input("기호를 입력하시오: ")
word=input("중간에 삽입할 문자열을 입력하시오: ")
s = str[:1] + word + str[1:]

print(s)