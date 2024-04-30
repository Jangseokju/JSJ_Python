# getter, setter
# - getter : 변수의 값를 가져오는 메소드
# - setter : 변수의 값을 지정하는 메소드

class Person:
    
    # getter
    def get_name(self):
        return self.name
    
    # setter
    def set_name(self, value):
        if len(value) >= 2:
            self.name = value
        else:
            print('이름은 2글자 이상이어야합니다')


p = Person()

p.name = 'ALOHA'
p.set_name('ALOHA')
print('p - name : {}'.format(p.name))

p.set_name('ALOHA')
print('p - name : {}'.format( p.get_name() ))


# 데코레이터를 이용한 getter, setter 정의

class Person:
    
    # @property : 해당 변수를 데코레이터 기능을 사용할수 있도록 지정 
    #             - 필드의 역할을 기능인 setter, getter 로 사용가능
    #             - @property 로 지정한 변수는 __변수 와같은 형태로 사용
    @property
    def name(self):
        return self.__name
    
    # @변수.setter  : 해당 메소드를 setter 메소드로 지정
    #                - (객체.변수 = 값) 문장실행 시,-->  지정한 setter 메소드가 실행
    @name.setter
    def name(self, value):
        self.__name = value
        print('setter 메소드 호출...')
        
    # @변수.getter  : 해당 메소드를 getter 메소드로 지정
    #                - (객체.변수) 문장실행 시,-->  지정한 getter 메소드가 실행
    @name.getter
    def name(self):
        print('getter 메소드 호출...')
        return self.__name
    
    
p = Person()

p.name = 'ALOHA'
print('p - name : {}'.format( p.name ))

p.__name = '직접 이름 지정'
print('p-name : {}'.format(p.__name))
        
        