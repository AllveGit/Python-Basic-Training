"""
===== 내장 함수 =====
"""

print("=" * 50)
print("Training_19. BuiltIn Function")

# abs
# 숫자 절댓값을 리턴해주는 함수
print(abs(3))
print(abs(-3))



# all
# 반복가능한 자료형(리스트, 튜플, 딕셔너리, 집합등)을 매개변수로 받으며, 매개변수의 요소가 모두 참인지 체크하는 함수 
allTest1 = [1, 2, 3, 0]
allTest2 = [1, 2, 3]
print(all(allTest1))
print(all(allTest2))



# any
# 반복가능한 자료형을 매개변수로 받으며, 매개변수의 요소중 하나라도 참이 있는지 체크하는 함수
anyTest1 = [0, 0, 0, 1]
anyTest2 = [0, 0, 0]
print(any(anyTest1))
print(any(anyTest2))



# chr
# 유니코드 값을 매개변수로 받아, 그 코드에 해당하는 문자를 리턴해주는 함수
print(chr(97))
print(chr(44032))



# ord
# 문자를 매개변수로 받아, 그 문자에 해당하는 유니코드 값을 리턴해주는 함수
print(ord('a'))
print(ord('가'))



# dir
# 객체를 매개변수로 받으며 그 객체가 자체적으로 가지고 있는 변수나 함수를 보여주는 함수
print(dir(1))
print("\n")
print(dir([1, 2, 3]))
print("\n")
print(dir({"1":'a'}))
print("\n")


# divmod
# 숫자 2개를 매개변수로 받으며, 그 두 숫자를 나눈 몫과 나머지를 튜플타입으로 리턴해주는 함수
print(divmod(7, 3))



# enumerate
# enum처럼 순서가 있는 자료형(리스트, 튜플, 문자열)을 매개변수로 받아 인덱스 값을 포함한 enum 객체를 리턴해주는 함수
for i, name in enumerate(["body", "foo", "bar"]):
    print(i, name)



# eval
# 실행가능한 문자열을 매개변수로 받아 문자열을 실행한 결과값을 리턴해주는 함수
print(eval("1+2"))
print(eval('"Hello" + "World"'))
print(eval("divmod(4, 3)"))



# filter
# 매개변수 두개를 받는다, 첫번째는 함수이름, 두번째는 반복이 가능한 자료형을 받는다.
# 첫번째 매개변수 함수에 두번째 자료형의 요소들이 하나씩 반복해서 들어가게 된다.
# 첫번째 매개변수 함수의 리턴값이 참인 요소들만 모아서(걸러서) 리턴해주는 함수
def IsBiggerThanThree(num):
    return num > 3

print(list(filter(IsBiggerThanThree, [1, -3, 2, 0, 5, 6, 4, 3, 10])))



# hex
# 정수값을 입력받아 16진수로 변환하여 리턴해주는 함수
print(hex(234))
print(hex(3))



# oct
# 정수값을 입력받아 8진수 문자열로 변환하여 리턴해주는 함수
print(oct(34))
print(oct(12345))


# id
# 객체를 입력받아 객체의 고유 주소 값을 리턴해주는 함수
idTest1 = 3
idTest2 = idTest1

# 모두 같다.
print(id(3))
print(id(idTest1))
print(id(idTest2))
# 다르다.
print(id(4))



# isinstance
# 매개변수를 두개 받는다. 첫번쨰는 인스턴스, 두번째는 클래스 이름을 받는다.
# 인스턴스가 클래스의 인스턴스인지 체크해주는 함수
class instanceTestClass:
    pass

instanceTest = instanceTestClass()
print(isinstance(instanceTest, instanceTestClass))



# map
# 매개변수를 두개 받는다. 첫번재는 함수, 두번째는 반복가능한 자료형을 받는다.
# 두번째 매개변수 자료형의 각 요소를 함수가 수행한 결과를 묶어서 리턴해주는 함수
def map_pow(num):
    return num * num

print(list(map(map_pow, [1, 2, 3, 4])))



# max
# 반복가능한 자료형을 매개변수로 받아 각 요소중 최댓값을 리턴해주는 함수
print(max([1, 2, 3]))
print(max("python"))



# min
# 반복가능한 자료형을 매개변수로 받아 각 요소중 최솟값을 리턴해주는 함수
print(min([1, 2, 3]))
print(min("python"))



# pow
# 매개변수를 두개 받는다. 첫번째 매개변수는 제곱할 숫자, 두번째 매개변수는 몇번 제곱할것인지 받는다.
# 숫자를 제곱한 결과값을 리턴해주는 함수
print(pow(2, 3))



# range
# 숫자를 매개변수로 받아 그 숫자만큼에 해당하는 범위 값을 반복할수 있는 값으로 만들어 리턴해주는 함수
print(list(range(5)))
# 세번째 매개변수는 숫자사이의 거리이다.
print(list(range(1, 10, 2)))



# sorted
# 순서가 있는 자료형을 매개변수로 받아 그 요소들을 정렬한 후 결과를 리스트로 리턴해주는 함수
# 리스트에 sort()가 있지만 그 리스트에서 자체적으로 정렬하기만 할뿐 정렬결과를 리턴해주지는 않는다는 점이 다르다.
print(sorted([3, 1, 2]))



# str
# str은 문자열 형태로 객체를 변환하여 리턴해주는 함수
print(str(3))



# sum
# 반복가능한 자료형을 매개변수로 받아 모든 요소들의 합을 리턴해주는 함수
print(sum([2, 4, 6]))



# type
# 객체를 매개변수로 받아 그 객체의 자료형이 무엇인지 알려주는 함수
print(type("abc"))
print(type(1))
print(type([1, 2, 3]))



# zip
# 동일한 개수로 이루어진 자료형의 가변인자를 매개변수로 받아 그 자료형들의 요소가 인덱스가 같은 요소끼리 묶어 리턴해주는 함수
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def", "ghi")))

print("=" * 50)