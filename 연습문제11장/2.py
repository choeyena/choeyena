infilename = input("파일 이름을 입력하시오: ").strip()
infile = open(infilename, "r")
file_s = infile.read() 
removed_s = input("삭제할 문자열을 입력하시오: ").strip()
modified_s = file_s.replace(removed_s, "")

infile.close() 
outfile = open(infilename, "w")

print(modified_s, file = outfile, end = "") 
print("변경된 파일이 저장되었습니다.") 
outfile.close() 