"""
===== 파일 입력과 출력 =====
"""

print("=" * 50)
print("Training_15. Class")

# 클래스 정의법

"""
# 클래스 함수의 첫번째 매개변수는 자기자신, 객체를 전달받는다.
# 함수를 사용할 때에는 첫번째 매개변수를 무시하고 사용하면 된다.
# 클래스 변수는 이 첫번째 매개변수를 이용하여 정의할수있다.
"""

class Test:
    def __init__(self):
        self.testResult = 0
        pass

    def func(self, num):
        self.testResult += num
        return self.testResult

classTest1 = Test()
print(classTest1.func(1))
print(classTest1.func(2))


print("=" * 50)