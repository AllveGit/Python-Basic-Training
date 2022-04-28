"""
===== 라이브러리 =====
"""

print("=" * 50)
print("Training_20. Default Library")

# ===== sys ======
"""
# sys 모듈은 python 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
"""

import sys

# sys.exit을 호출하면 강제로 스크립트를 종료한다.
# sys.exit()

# sys.path는 파이썬 모듈들이 저장되어있는 위치들을 리턴해준다.
print(sys.path)



# ===== Pickle =====
"""
Pickle 모듈은 객체의 형태를 그대로 유지하며 파일에 저장하고 불러올 수 있게 하는 모듈
"""

import pickle

# wb는 바이너리 형식으로 작성하는 모드이다.
pickleWriteFile = open("pickleTestFile.txt", 'wb')
pickleFileWriteData = {1: "python", 2: "you need"}

# pickle.dump를 호출하면 객체를 그대로 파일에 저장할 수 있다.
pickle.dump(pickleFileWriteData, pickleWriteFile)
pickleWriteFile.close()

# rb는 바이너리 형식으로 읽는 모드이다.
pickleReadFile = open("pickleTestFile.txt", 'rb')

# pickle.load를 호출하면 객체를 그대로 하나씩 불러올 수 있다.
pickleReadData = pickle.load(pickleReadFile)
print(pickleReadData)

pickleReadFile.close()



# ===== OS =====
"""
OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈
"""

import os

# os.environ을 호출하면 시스템의 환경변수값을 리턴해준다.
print(os.environ)

# os.chdir을 호출하면 현재 프로젝트의 디렉터리 위치를 변경할 수 있다.
# os.chdir("C:\PYTHON")

# os.getcwd를 호출하면 현재 자신의 디렉터리 위치를 리턴해준다.
print(os.getcwd())

# os.system를 호출하면 시스템 명령어를 파이썬에서 호출할 수 있다.
# os.system("dir")

# os.popen을 호출하면 시스템 명령어를 실행한 결과값을 읽기 모드 형태의 파일 객체로 돌려준다.
# f = os.popen("dir")
# f.close()

# os.mkdir을 호출하면 새 디렉터리를 생성한다.
# os.mkdir("NewDirectory")

# os.rmdir을 호출하면 디렉터리를 지운다. 단, 디렉터리가 비어있어야 지울 수 있다.
# os.rmdir("NewDirectory")

# os.unlink를 호출하면 파일을 지운다.
# os.unlink("pickleTestFile.txt")

# os.rename을 호출하면 두번째 매개변수의 이름으로 파일 이름을 바꾼다.
# os.rename("testFile.txt", "testFile2.txt")



# ===== shutil =====
"""
shutil은 파일을 복사해주는 파이썬 모듈이다.
"""

import shutil

# shutil.copy(src, dst)를 호출하면 
# dst가 파일이름이면, src라는 이름의 파일을 dst라는 이름의 파일로 복사한다.
# dst가 디렉터리이름이면 src라는 이름의 파일을 dst 디렉터리에 복사한다.
shutil.copy("testFile.txt", "testFile2.txt")



# ===== glob =====
"""
특정 디렉터리에 있는 파일 이름 모두를 알아야할때 사용하는 모듈이다.
"""

import glob

# glob.glob을 호출하면 디렉터리 안에 있는 파일, 디렉터리들의 경로들을 모두 모아 리스트로 만들어준다.
print(glob.glob("source/*"))



# ===== tempfile =====
"""
파일을 임시로 만들어서 사용할때 유용한 모듈이다.
"""

import tempfile

# tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 리턴해준다.
filename = tempfile.mkstemp()
print(filename)

# tempfile.TemporaryFile()는 임시 저장공간으로 사용할 파일 객체를 리턴해준다. 기본적으로 wb 모드를 갖는다.
# 이 파일 객체의 close가 호출되면 파일 객체는 자동으로 소멸한다.
tempF = tempfile.TemporaryFile()
tempF.close()



# ===== time =====
"""
시간과 관련된 작업을 할때 사용하는 모듈이다.
"""

import time

# time.time을 호출하면 UTC를 사용한 시간을 실수형으로 리턴해준다.
print(time.time())

# time.localTime을 호출하면 time.time()이 리턴해준 값을 매개변수로 받아 연도, 월, 일, 시, 분, 초 형태로 바꾸어준다.
print(time.localtime(time.time()))

# time.asctime을 호출하면 time.localtime()이 리턴해준 튜플 값을 보기 쉬운 형태로 바꾸어준다.
print(time.asctime(time.localtime(time.time())))

# time.ctime을 호출하면 time.asctime(time.localtime(time.time()))이랑 똑같은 결과를 리턴한다.
# 단, 현재시간만 리턴해준다.
print(time.ctime())

# time.strftime을 호출하면 시간표현에 포맷을 주어 변환하게 할 수 있다.
# 포맷이 무엇들이 있는지는 이 사이트에서 스크롤하여 내려보면 된다. https://wikidocs.net/33
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))

# time.sleep을 호출하면 일정한 시간 간격동안 스레드가 멈춘다.
time.sleep(1)
print("1 sec delay!")



# ===== calendar =====
"""
파이썬에서 달력을 볼 수 있게 해주는 모듈이다.
"""

import calendar

# calendar.calendar(year)를 호출하면 그해의 전체달력을 볼 수 있다.
print(calendar.calendar(2022))

# calendar.prmonth(year, month)를 호출하면 특정해의 특정달의 달력을 볼 수 있다.
print(calendar.prmonth(2022, 4)) 

# calendar.weekday(year, month, day)를 호출하면 그 날짜에 해당하는 요일 정보를 리턴해준다. 월요일은 0, 일요일은 6이다.
print(calendar.weekday(2022, 5, 5))

# calendar.monthrange(year, month)를 호출하면 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지 튜플로 리턴해준다. 
print(calendar.monthrange(2022, 4))



# ===== random =====
"""
난수를 발생시키는 모듈이다.
"""

import random

# random.random()을 호출하면 0.0~1.0 사이의 실수인 난수를 리턴해준다.
print(random.random())

# random.randint()를 호출하면 매개변수1~매개변수2 사이의 정수인 난수를 리턴해준다.
print(random.randint(1, 10))

# random.choice()를 호출하면 순서가 있는 자료형을 매개변수로 받아 요소를 랜덤으로 리턴해준다.
randChoiceTest = [1, 2, 3, 4, 5]
print(random.choice(randChoiceTest))

# random.shuffle()을 호출하면 순서가 있는 자료형을 매개변수로 받아 요소들의 순서를 랜덤으로 섞는다.
randShuffleTest = [1, 2, 3, 4, 5]
random.shuffle(randShuffleTest)
print(randShuffleTest)

print("=" * 50)