infile = open(filename, "r") 
for line in infile:
      ...
def countLine(line, counter):
     for ch in line:
         if ch.isalpha():
                 if ch in counter:
                         counter[ch] = counter[ch] + 1
                 else:
                         counter[ch] = 1
                         
fname = input("입력 파일 이름: ").strip()
infile = open(fname, "r") 

my_dict = { } 
for line in infile:
         countLine(line, my_dict)
         
print(my_dict)
infile.close()