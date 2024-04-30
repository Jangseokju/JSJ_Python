# Person 클래스 선언
class Person:
    
    # name = '이름없음'
    # age = 0
    # tel = '010-0000-0000'
    
    # 생성자
    # 파이썬에서는 생성자는 여러 개 정의할 수 없다.(오버로딩X)
    # def __init__(self):
    #     print('Person 객체 생성...')
        
    # 생성자
    # - 정의한 생성자의 매개변수에 디폴트매개변수를 설정하여 오버로딩처럼 구현한다
    def __init__(self=None, name=None, age=None, tel=None):
        self.name = name
        self.age = age
        self.tel = tel
        print('Person 객체 생성...')
        
    # 소멸자
    def __del__(self):
        print('Person 객체 소멸...')
        
    # 메소드
    def show_info(self):
        print('이름 : {}, 나이 : {}, 전화번호 : {}'.format(self.name, self.age, self.tel))
    

# Person 객체 생성
person = Person()

# 객체의 변수 접근
person.name = '마동석'
person.age = 20
person.tel = '010-1234-1234'

print('이름 :', person.name)
print('나이 :', person.age)
print('전화번호 :', person.tel)


person2 = Person('손석구', 20, '010-1111-2222')
print( person2.name )
print( person2.age )
print( person2.tel )


person3 = Person('조승우', 30, '010-0000-0000')
person3.show_info()
