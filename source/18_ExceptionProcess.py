"""
===== 예외 처리 =====
"""

print("=" * 50)
print("Training_18. Exception Process")

"""
# C++, C#에서 쓰는 try-catch처럼 python에서도 예외처리를 하는 문법이 있다.
# try, except문이다.
"""

# try, except, finally문 정의법

# try, except만 쓰는 경우, 모든 오류를 except에서 받는다.
f1 = open("testFile.txt", 'r')
try:
    line = f1.readline()
    print(line)
except:
    print("Exception!!!")
finally:
    f1.close()

# except에 발생 오류 타입만 포함한 경우는 이 발생 오류 타입에 한한 오류들만 except문에서 받는다.
f2 = open("testFile.txt", 'r')
try:
    line = f2.readline()
    print(line)
except IndexError:
    print("Index Exception!!!")
finally:
    f2.close()

# except에 발생 오류 타입과 오류 메시지 변수까지 포함한 경우는 오류 로그 까지 알고 싶을때 사용한다.
f3 = open("testFile.txt", 'r')
try:
    line = f3.readline()
    print(line)
except IndexError as IndexErrMsg:
    print("Index Exception!!! Log : %s" % IndexErrMsg)
finally:
    f3.close()

# 발생 오류 타입으로 여러개의 타입의 오류를 잡을 수 있다.
f4 = open("testFile.txt", 'r')
try:
    line = f4.readline()
    print(line)
    4/0
except IndexError as e:
    print("Index Exception!!! Log : %s" % e)
except ZeroDivisionError as e:
    print("ZeroDivision Exception!!! Log : %s" % e) 
finally:
    f4.close()

f5 = open("testFile.txt", 'r')
try:
    a = [1, 2]
    print(a[3])
except (IndexError, ZeroDivisionError) as e:
    print("Exception!!! Log : %s" % e)
finally:
    f5.close()



# except문에 else를 넣으면 오류가 없을 때 수행된다. 
try:
    a = [1, 2]
    print(a[0])
except IndexError as e:
    print("Index Exception! Log : %s" % e)
else:
    print("No Error!")    



# except문에 pass를 사용하면 그냥 오류를 무시하고 넘어간다.



# 오류 일부러 발생시키기
"""
# 예를 들어, c++의 순수 가상 함수처럼 구현하고 싶은 함수가 있다면
# 자식 클래스가 부모 클래스의 함수를 구현하지 않으면 에러를 내야 한다. 그렇기에 자식클래스에 구현하지 않고 사용한다면 오류를 일부러 발생시켜야 한다는 의미이다. 
# 게다가 프로그램이 의도한대로 돌아가게 하기 위해 일부러 에러를 내야할 상황이 있다.
"""

# 이때 사용하는 것이 raise문이다.
# raise문은 프로그램에 에러를 발생시키는 명령어다.

class Parent:
    def PureFunc(self):
        raise NotImplementedError

class Child(Parent):
    pass

c = Child()
# 이렇게 함수를 오버라이드하여 구현하지 않으면 NotImplementedError가 발생할 것이다.
# c.PureFunc()



# Exception 커스텀 만들기
# Exception 상속받아 클래스로 만든다
class MyError(Exception):
    # Exception에서 이 함수가 에러메시지를 전달하는 함수이다.
    # 구현하지 않으면 에러메시지가 출력되지 않는다.
    def __str__(self):
        return "파이썬이 아닙니다!"

def python_check(InType):
    if InType == "python":
        print("PYTHON")
    else:
        raise MyError()

try:
    python_check("python")
    python_check("c++")
except MyError as e:
    print(e)

print("=" * 50)
