"""
===== 반복문 : for =====
"""

print("=" * 50)
print("Training_11. for")

# C#의 foreach 같이 사용
# c++의 ForRange 같이 사용

# for을 제어할 때도 while문과 똑같이 break, continue 사용

# for 정의법 
test_list = [1, 2, 3, 4, 5]
for i in test_list:
    print(i)

test_list2 = [(1,2), (3,4), (5,6)]
for (i, j) in test_list2:
    print(i + j) 



# for문과 자주 사용하는 range 함수
# range 객체 생성
rangeObjTest1 = range(10)
rangeObjTest2 = range(1, 11)
print(rangeObjTest1)
print(rangeObjTest2)

rangeResTest = 0
# range를 이용하면 c++ for처럼 몇번 돌지 정할 수 있음 
for i in range(1, 11):
    rangeResTest = rangeResTest + i

rangeTest = [1, 2, 6, 8, 214039, 4]
for i in range(len(rangeTest)):
    if rangeTest[i] < 5:
        continue

    print("range for loop!!!!!")



# 리스트 내포 사용하기
# 리스트안에 for문을 포함하여 생성하는 리스트 내포방법이 있다.

# 일반적인 for문
listForTest1 = [1,2,3,4]
listForResult1 = []

for i in listForTest1:
    listForResult1.append(i * 3)

print(listForResult1)

# 리스트내포 for문
# [표현식 for 항목 in 반복가능객체 if 조건문] 이 폼이다.
listForTest2 = [1,2,3,4]
listForResult2 = [i * 3 for i in listForTest2]
print(listForResult2)

listForTest3 = [1,2,3,4]
listForResult3 = [i * 3 for i in listForTest3 if i % 2 == 0]
print(listForResult3)

# for문 여러개도 가능
# 구구단 예제
multiplyTable = [i * j for i in range(2, 10)
                       for j in range(1, 10)]
print(multiplyTable)

print("=" * 50)