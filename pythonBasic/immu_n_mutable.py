"""
    Topic : 파이썬의 불변타입과 가변타입에 대한 정리
    불변타입 : 메모리 상에서 변수가 차지하는 자리의 값이 바뀌지 않음
            -> 따라서 변수의 값이 변경될 경우, 다른 자리에 값을 저장하고, 변수의 레퍼런스를 해당 자리로 변경시킴
            - 종류 : 수, 문자열, 튜플
    가변타입 : 메모리 상에서 변수가 차지하는 자리의 값이 바뀜
            -> 따라서 변수의 값이 변경될 경우, 해당 변수가 레퍼런스하는 자리의 값이 바뀌고, 레퍼런스 자리또한 유지됨

    cf) Java에는 int, float등이 기초타입이고, 객체로 되어있는 레퍼런스 타입이 따로있지만, 파이썬에선 모든 것이 객체다.
"""
# 불변타입
print("1) 숫자")
a = 3
print(f"a의 id는 {id(a)}입니다.")
a = 4
print(f"a 변경 후 id는 {id(a)}입니다.")

print("2) 문자열")
s = 'spring'
print(f"s의 id는 {id(s)}입니다.")
s = 'summer'
print(f"s 변경 후 id는 {id(s)}입니다.")

print("3) 튜플")
t = (1, 2, 3)
print(f"t의 id는 {id(t)}입니다.")
t = (3, 4, 5)
print(f"t의 변경 후 id는 {id(t)}입니다.")



# 가변타입과 불변 타입
fruits = ['apple', 'banana']
print(id(fruits))
print(id(fruits[0]))
fruits[0] = 'cherry'
print(id(fruits))
print(id(fruits[1]))
# 결론 : 리스트의 레퍼런스는 변경되지 않지만, 리스트 안의 값의 레퍼런스는 변경된다.
