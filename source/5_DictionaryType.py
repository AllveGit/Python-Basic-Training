"""
===== 튜플 자료형 =====
"""

print("=" * 50)
print("Training_5. DictionaryType")

# 딕셔너리 정의법
# {} 대괄호로 둘러쌓으며, 그안에 Key:Value의 폼으로 요소들을 넣는다. Value에 리스트를 넣는것도 물론 가능하다.
dictionaryTest1 = {"name":"SeungJae", "email":"allvegamedevelop@gmail.com", "birth":"0815"}
dictionaryTest2 = {"Ye":[1, 2, 3]}
print(dictionaryTest1)
print(dictionaryTest2)



# 딕셔너리 쌍 추가하기
dictionaryAddTest = {"Test":"Wow"}
# 그냥 첨자연산자에 키를 넣고 값을 대입해주면 쌍이 추가된다.
dictionaryAddTest["Test2"] = "Wow2"
print(dictionaryAddTest)
dictionaryAddTest["Test3"] = ['W', 'O', 'W', 3]
print(dictionaryAddTest)



# 딕셔너리 요소 삭제하기
dictionaryDelTest = {1:10, 2:20, 3:30, 4:40}
del dictionaryDelTest[2]
print(dictionaryDelTest)



"""
# 딕셔너리 만들때 주의사항
# Key는 고유기 때문에 중복키가 있으면 마지막 키를 제외한 나머지 키들은 무시가 된다.
# 변하지않는 값 Tuple은 Key로 쓸 수 있지만, List는 키로 쓸 수 없다. List를 키로 쓰면 에러가 발생한다.
"""



# 딕셔너리 관련 함수들 (keys, values, items, clear, get, in)

# keys는 딕셔너리 요소들의 키를 모두 모아 dict_keys 객체를 리턴해주는 함수이다.
# dict_keys? 원래 2.7버전까지는 리스트를 리턴해주었지만 메모리 낭비를 줄이기 위해 변경. 리스트로 변환하지않더라도 기본적인 반복구문은 사용가능.
# list 변환은 list(dictionaryKeysTest.keys())로 하면 된다.
dictionaryKeysTest = {"key1":"value1", "key2":"value2", "key3":"value3"}
print(dictionaryKeysTest.keys())



# values는 keys와 반대로 value들만 모아 dict_values 객체를 리턴해주는 함수이다.
dictionaryValuesTest = {"key1":"value1", "key2":"value2", "key3":"value3"}
print(dictionaryValuesTest.values())



# items는 keys와 values를 모두 합친 것으로 key, value 모두 모아 dict_items 객체를 리턴해주는 함수이다.
dictionaryItemsTest = {"key1":"value1", "key2":"value2", "key3":"value3"}
print(dictionaryItemsTest.items())



# clear는 Dictionary안의 모든 요소를 삭제하는 함수이다.
dictionaryClearTest = {"key1":"value1", "key2":"value2", "key3":"value3"}
dictionaryClearTest.clear()
print(dictionaryClearTest)



# get은 key로 value를 얻어오는 함수이다.
# 이미 첨자연산자로 value를 가져올 수 있지만, 첨자연산자에서 가져올 때 존재하지 않는 키를 가져온다면 에러가 발생하지만, get으로 가져오면 에러가 발생하지않고 None을 리턴해준다.
dictionaryGetTest = {"key1":"value1", "key2":"value2", "key3":"value3"}
print(dictionaryGetTest.get("key2"))
print(dictionaryGetTest.get("key4"))
# 딕셔너리 안에 찾으려는 key값이 없을 경우 미리 정해둔 디폴트값을 가지고 오게 할수도 있다.
# 이 구문은 키를 못찾으면 -1이라는 값을 가져오라고 설정한 구문이다.
print(dictionaryGetTest.get("key4", -1))



# in은 해당 Key가 딕셔너리 요소중에 존재하는지 체크하는 함수이다.
dictionaryInTest = {"key1":"value1", "key2":"value2", "key3":"value3"}
print("key1" in dictionaryInTest)
print("key4" in dictionaryInTest)

print("=" * 50)