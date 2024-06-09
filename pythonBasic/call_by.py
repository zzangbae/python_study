"""
    Topic : 파이썬의 함수 호출
    호출의 종류
    1) 복사호출 : 함수로 주이지는 인자가 갑이 복사되어 들어옴.
            - 따라서 해당 변수 값을 변경해도 인자로 들어간 기변수의 값은 바뀌지 않음
            - 만약 값을 바꾸길 원한다면, return값으로 받아서 변수에 재할당해야함
            - 인자가 불변타입을 경우 복사호출을 활용한다(in python)
                - 불변타입 -> 자리의 값을 바꿀 수 없음 -> 따라서 값을 복사함
    2) 참조호출 : 함수로 주어지는 인자가 레퍼런스 값으로 들어옴
            - 따라서 해당 변수 값을 변경하면 기변수의 값 또한 바뀜
            - 인자가 가변타입을 경우 참조호출을 활용함(in python)
    3) 할당호출 = 복사호출 + 참조호출
            - 함수의 매개변수로 들어오는 값이 가변타입인지 불변타입인지에 따라 호출방식이 변경됨
            - 불변타입 : 복사호출
            - 가변타입 : 참조호출
"""
# 복사 호출 되는 경우
def plus3(a):
    a = a + 3

def plus3return(a):
    a = a + 3
    return a

a = 3
plus3(a)
print(a)    # 3

a = plus3return(a)
print(a)    # 6

# 참조호출의 경우
x = 5
y = [1, 2]

def f(x, y):
    x = x + 5
    y.append(x)

f(x, y)
print(f"x = {x}")   # 5 : 불변타입인 숫자는 복사호출이 되기 때문에 값이 변경되지 않음
print(f"y = {y}")   # [1, 2, 10] : 가변타입인 리스트는 참조호출되기 때문에 값이 변경됨
# 위와 같이 인자의 변수타입(가변 or 불변)에 따라서 함수의 인자 호출방식이 다른 것을 "할당호출"이라고 명명됨(call-by-assignment)