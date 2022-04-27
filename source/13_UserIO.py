"""
===== 사용자 입력과 출력 =====
"""

print("=" * 50)
print("Training_13. UserIO")

# scanf처럼 input받기
# input은 입력하는 모든 걸 문자열로 취급하기에 리턴값도 무조건 문자열이다.
inputTestStr = input()
print(inputTestStr)

# input안에 문자열을 넣으면 그 문자열을 출력 후, 입력을 받을 수 있다.
inputTestStr2 = input("입력하세요 : ")
print(inputTestStr2)

# 한 줄에 결과 값 출력하기
for i in range(10):
    if i == 9:
        print(i)
    else:
        print(i, end=' ')

print("=" * 50)