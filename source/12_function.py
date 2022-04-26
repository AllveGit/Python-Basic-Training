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

print("=" * 50)