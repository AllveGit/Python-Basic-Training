"""
===== 패키지 =====
"""

print("=" * 50)
print("Training_17. Package")

"""
# 패키지는 파이썬 모듈들을 계층적으로 관리할 수 있게 해준다.
# C#의 패키지처럼 도트(.)를 통하여 관리한다.
# ex) Apple.iphone -> Apple = 패키지, iphone = 모듈 
"""

# Python 패키지는 디렉터리와 파이썬 모듈로 이루어진다. (C#이랑 똑같음)
# 패키지에서 모듈을 불러오는 방법들이다.

import TestPackage.client.clientModule
TestPackage.client.clientModule.client_test()

from TestPackage.client import clientModule
clientModule.client_test()

from TestPackage.client.clientModule import client_test
client_test()

# 하지만 패키지만 임포트해서 모듈을 불러올 수는 없다.
# import TestPackage를 수행하면 TestPackage 디렉터리의 __init__.py에 정의된 것만 참조가능 
import TestPackage
TestPackage.client.clientModule.client_test()

# 도트 연산자(.)를 사용해서 import할 때 가장 마지막 항목은 반드시 모듈 또는 패키지여야만 한다.



# __init__.py 의 용도
"""
# 이 파일이 있는 디렉터리는 패키지의 일부임을 알려주는 역할을 한다.
# python은 이 파일이 있어야 패키지로 인식을 한다.
"""

# 아무 설정을 하지 않고 이런식으로 임포트하면 에러가 날 것이다.
from TestPackage.client import *
"""
# 에러가 나는 이유는 패키지나 디렉터리를 *을 사용하여 import할 때에는 
# 그 디렉터리의 __init.py__ 파일에 __all_ 변수에 import할 수 있는 모듈을 정의해주어야 인식할 수 있기 때문이다.
# 이 규칙이 적용되는 경우는 임포트할때 도트 연산자의 가장 마지막 항목이 모듈이 아닌 경우이다.
"""

print("=" * 50)