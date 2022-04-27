"""
===== 파일 입력과 출력 =====
"""

print("=" * 50)
print("Training_14. FileIO")

# 파일 생성 하는 법
"""
# open() 함수를 이용하면 파일 생성 가능
# 파일 열기 모드 'w' = 쓰기 모드 (파일에 내용을 쓸 때 사용)
# 파일 열기 모드 'r' = 읽기 모드 (파일에 내용을 읽기만 할 때 사용)
# 파일 열기 모드 'a' = 추가 모드 (파일의 마지막에 새로운 내용을 추가할 때 사용)
"""
f = open("testFile.txt", 'w')

# 닫지 않더라도 파이썬이 종료될때 자동으로 닫아주지만 쓰기모드로 열였던 파일을 닫지 않고 다시 열려고 하면 에러가 나기 때문에 닫아주는게 좋음
f.close()



# 파일 쓰는 법 
f = open("testFile.txt", 'w')

for i in range(10):
    strData = "%d line. \n" % i
    # write 함수를 이용하면 파일에 작성할 수 있다.
    f.write(strData)

f.close()



# 파일 읽는 법
f = open("testFile.txt", 'r')

# readline은 파일의 한줄을 읽는 함수이다. 그러므로 문자열이 더 이상 안 읽힐 떄까지 읽는다.
while True:
    readLine = f.readline()
    if not readLine: 
        break

    print(readLine)

f.close()

# readlines는 파일의 모든 줄을 읽어 각각의 줄을 요소로 리스트를 만들어 돌려주는 함수이다.
f = open("testFile.txt", 'r')

readLines = f.readlines()
for readLine in readLines:
    readLine = readLine.strip()  # 줄 끝의 줄 바꿈 문자 제거
    print(readLine)

f.close()

# read 함수는 파일 전체의 내용을 문자열로 리턴해주는 함수이다.
f = open("testFile.txt", 'r')

fileStr = f.read()
print(fileStr)

f.close()



# 파일 새로운 내용 추가하는 법
f = open("testFile.txt", 'a')

newLine = "New Line! \n"
f.write(newLine)

f.close()



# with
# go의 defer과 같이 파일을 자동으로 닫을때 사용하는 명령어이다.
# 이런식으로 with문이 끝나면 자동으로 f(파일)를 닫아준다.
with open("testFile.txt", 'w') as f:
    f.write("With case test")



# sys module로 매개변수


print("=" * 50)