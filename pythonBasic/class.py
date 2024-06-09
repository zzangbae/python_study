"""
    Topic : 클래스(Class)
    클래스란? 객체를 만드는 틀
    ex) 호두과자(객체)를 만드는 호두과자틀(클래스, 주형)

    클래스 내에서 각 변수의 위치에 따라서 변수의 커버리지가 어떻게 되는지 알아보고자 함
"""
class Person:
    team_point = 0  # 클래스로 만들어진 객체들이 모두 공유하는 변수. Person.{변수명}으로 접근해야한다. "클래스 전역변수"
    def __init__(self, name, age):
        self.name = name    # 클래스로 만들어진 객체 하나에 한정된 "갹채 자역 변수"
        self.age = age
        self.personal_point = 0
        self.__secret = "secret"    # 비공개
    def get_point(self):
        self.personal_point += 1
        # self.team_point += 1  # self.team_point로 하면 Person.team_point는 안오른다. -> 다르게 취급된다.
        # 따라서 위와 같이 쓰는 것은...예기치 않는 오류를 생성할 가능성이 높아진다.
        Person.team_point += 1  # 이렇게 하면 self.team_point도 오른다.

    def insert_age(self, age):
        self.__fight()
        self.__plus_age(age)

    # 비공개 메서드 -> 클래스 밖에는 공개되지 않음
    def __plus_age(self, age):
        self.age = age

    def __fight(self):
        print("!!!!!!!!!!gooood!!!!!!!!!!")

p1 = Person("John", 24)
p2 = Person("Smith", 25)

print(f"팀점수 : {Person.team_point}")
print(f"p1의 개인점수 : {p1.personal_point}")
print(f"p2의 개인점수 : {p2.personal_point}")

print(f"{p1.get_point()}-- 점수 획득 --")
print(f"팀점수 : {Person.team_point}")
print(f"p1이 아는 팀점수 : {p1.team_point}")
print(f"p1의 개인점수 : {p1.personal_point}")
print(f"p2의 개인점수 : {p2.personal_point}")

print(f"Person.team_point의 id : {id(Person.team_point)}")
print(f"p1.team_point의 id : {id(p1.team_point)}")
print(f"p2.team_point의 id : {id(p2.team_point)}")

print()
print(f"공개된 변수를 불러보자 : {p1.age}")
# print(f"비공개 변수를 불러보자 : {p1.__secret}")    -> 오류가 뜨게 된다. 클래스 밖에서 공개할 필요가 없는 변수
p1.insert_age(4)
print(f"p1의 나이 : {p1.age}")
# p1.__fight()    -> 오류가 뜨게 된다. 비공개 메서드. 하지만, 클래스 메서드가 수행되는 중간과정에서 수행되었다.


"""
    만약 클래스 변수를 self.{클래스변수명}으로 취급하게 될 경우,
    취급이 포함된 메서드가 실행될 때, 해당 객체에 대한 클래스 변수는 객체 지역변수처럼 취급되게 된다.
    따라서 클래스 변수를 활용할 때는 {클래스명}.{클래스변수명}으로 사용하는 것이 좋다.
    아니면 예기치 않은 오류가 생성될 것....
"""



