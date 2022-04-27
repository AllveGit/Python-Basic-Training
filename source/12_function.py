"""
===== 함수 =====
"""

print("=" * 50)
print("Training_12. function")

# 함수 정의법
"""
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
"""

# 함수를 정의하고 사용
def func1(a):
    print(a)

func1(1)

# 함수 리턴 값을 받기
def func2(a, b):
    return a + b

print(func2(2, 3))

# 함수에 리턴값이 없는데 리턴을 받으면 None을 받는다.
def func3():
    print("Return None!!")


func3ReturnValue = func3()
print("func3 return value : ", end="")
print(func3ReturnValue)

# 매개변수를 지정하여 호출할수도 있다.
def func4(a, b):
    print(a)
    print(b)

func4(a=3, b=7)



# 가변인자 함수
# 매개변수 이름앞에 *을 붙이면 입력값을 전부모아 튜플로 만들어줌
def vaFunc1(*args):
    result = 0
    for i in args:
        result += i

    return result

print(vaFunc1(1, 2, 3, 4, 5))
print(vaFunc1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 여러 개의 매개변수도 포함이 가능하지만, 가변인자가 매개변수중 맨 마지막에 위치하여야한다.
def vaFunc2(condition, *params):
    result = 0

    if condition == "GOOD":
        for i in params:
            result = result + i
    elif condition == "BAD":
        for i in params:
            result = result - i

    return result

print(vaFunc2("GOOD", 1, 2, 3, 4, 5))
print(vaFunc2("BAD", 1, 2, 3, 4, 5))

# 키워드 가변인자 함수
# 매개변수 이름 앞에 **을 붙이면 입력값을 전부 모아 딕셔너리로 만들어줌
def vaFunc3(**args):
    print(args)

vaFunc3(a=1, b=2, Three=3, Four="Four")



# 다른 언어들처럼 매개변수에 초깃값을 미리 세팅할수도 있다.
def AlreadySetFunc(a, b, c = 3):
    print("%d %d %d" % (a, b, c))

AlreadySetFunc(1, 2)



# 람다 함수
# 람다로 만든 함수는 return 명령어가 없어도 결과 값을 리턴해줌
addLambda = lambda a, b: a+ b
print(addLambda(3, 4))

print("=" * 50)