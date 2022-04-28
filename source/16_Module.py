"""
===== 모듈 =====
"""

print("=" * 50)
print("Training_16. Module")

# 모듈은 지금 작성하고 있는 파일 .py 확장자가 붙은 파일들을 말한다.

# 모듈 불러오는 법
# TestModule1이라는 모듈을 불러온다.
# 이런식으로 모듈을 불러오면 모듈에 있는 함수를 꺼내기 위해서는 모듈의이름.함수 같은 형식으로 호출해야한다.
import TestModule1
print(TestModule1.add(1, 2))

# TestModule1 이라는 모듈에서 add 함수를 불러온다.
# 이런식으로 불러오면 앞에 모듈의 이름을 붙일 필요없이 함수만 호출해도 모듈의 함수가 불린다.
from TestModule1 import add
print(add(1, 2))

# TestModule1 모듈은 add, sub 함수가 있는데 둘다 불러오려면 두가지 방법이 있다.
# 이렇게 두가지 함수만 불러오거나
from TestModule1 import add, sub
# *을 붙여 TestModule1의 모든 함수를 불러오게 할 수 있다.
from TestModule1 import *



# if __name__ == "__main__" 의 의미
# TestModule2를 불러오기만 했는데 TestModule2에서의 print구문이 실행되어버린다.
import TestModule2

# 이를 방지하기 위해 if __name__ == "__main__"을 쓴다.
# 직접 파일을 실행하면 __name__ 값이 __main__이 되지만, 모듈로 불러서 사용할 때는 __name__ 값이 __main__이 아닌 모듈의 이름이 된다.
# 이를 이용하여 수정한 것이 TestModule3이다.
import TestModule3



# 모듈안에 있는 클래스나 변수들도 불러올 수 있다.
import TestModule4
print(TestModule4.PI)

moduleClassTest = TestModule4.Math()
print(moduleClassTest.PIMultiply(3))


"""
# 지금까지 모듈의 불러오는 법을 적용시키기 위해서는 모듈들이 같은 디렉터리에 있어야 한다.
# 다른 디렉터리에서 불러올 수 있게 하려면 sys.path.append를 이용하거나 PYTHONPATH 환경변수에서 디렉터리 경로를 추가해야한다.
"""

print("=" * 50)