"""
===== 파일 입력과 출력 =====
"""

from copyreg import constructor


print("=" * 50)
print("Training_15. Class")

# 클래스 정의법

"""
# 클래스 함수의 첫번째 매개변수는 자기자신, 객체를 전달받는다.
# 함수를 사용할 때에는 첫번째 매개변수를 무시하고 사용하면 된다.
# 클래스 변수는 이 첫번째 매개변수를 이용하여 정의할 수있다.
"""

class Test:
    def __init__(self):
        self.testResult = 0

    def func(self, num):
        self.testResult += num
        return self.testResult

classTest1 = Test()
print(classTest1.func(1))
print(classTest1.func(2))



# 클래스 생성자
class ConstructorTest:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def func(self):
        print(self.first)
        print(self.second)

constructorTest = ConstructorTest(10, 20)
constructorTest.func()



# 클래스 상속
# 클래스 정의할떄 ()안에 부모클래스를 넣어준다. , 으로 다중상속 가능
class ParentTest:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def func(self):
        print(self.first)
        print(self.second)

class ChildTest(ParentTest):
    def __init__(self, first, second, three):
        # super로 부모 클래스 접근 가능
        super().__init__(first, second)
        # 다중상속을 했을 때에는 Super가 아닌 이런식으로 직접 부모클래스 접근
        # ParentTest.__init__(first, second)
        self.three = three

    # 메서드 오버라이드
    def func(self):
        print(self.first + self.second + self.three)

parentTest = ParentTest(1, 2)
childTest = ChildTest(1, 2, 3)

parentTest.func()
childTest.func()



# 클래스 변수
"""
# 객체는 다른 객체들에 영향받지 않고 객체마다 다른 값을 띌 수 있다.
# 클래스 변수는 그 클래스로 만든 객체가 모두 영향을 받는 변수이다.
#
"""

class ClassVariableTest:
    Value1 = "AAA"

classVariableTest1 = ClassVariableTest()
classVariableTest2 = ClassVariableTest()

print(classVariableTest1.Value1)
print(classVariableTest2.Value1)

ClassVariableTest.Value1 = "BBB"

print(classVariableTest1.Value1)
print(classVariableTest2.Value1)

# 이렇게 객체에서 클래스 변수를 바꾸게 되면 클래스변수가 바뀌는 것이 아닌 Value1이라는 새로운 객체변수를 생성시킨다
classVariableTest1.Value1 = "AAA"

print(classVariableTest1.Value1)
print(classVariableTest2.Value1)

print("=" * 50)