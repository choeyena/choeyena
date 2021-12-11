def sumProblem(x, y):
    sum = x + y
    sentence = "정수" + str(x) + "+"+str(y)+"의 합은?"
    print(sentence)
    
def main():
    a = int(input("첫 번째 정수: "))
    b = int(input("두 번째 정수: "))
    sumProblem(a, b)
    
main()