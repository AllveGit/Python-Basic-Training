"""
===== 반복문 : while =====
"""

print("=" * 50)
print("Training_10. while")

# if처럼 : 이후로 문장마다 들여쓰기(tab) 필요
# 들여쓰기를 하지 않으면 while문안에 포함이 되지않음.

# while문 정의법
damage = 0
while damage < 10:
    damage += 1

    if damage == 10:
        print("10데미지를 주어 처치하였습니다.")
    else:
        print("%d 데미지 차징~~" % damage)



# while 제어

# break
breakCnt = 0
while breakCnt < 3:
    breakCnt += 1
    if breakCnt == 2:
        break

    print("break 안탔어요~")

# continue
continueCnt = 0
while continueCnt < 3:
    continueCnt += 1
    if continueCnt == 2:
        continue
    
    print("continue 안탔어요~")

print("=" * 50)