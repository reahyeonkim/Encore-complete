# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:03:35 2021

@author: Playdata
"""

# 인자가 없고 리턴값이 없는 함수
def my_fnc():
    print("첫 번째 인자가 없는 함수")

my_fnc()

# 인자가 있고 리턴 값이 없는 함수
def my_fnc2(name):
    print("전달된 이름은 {} 입니다 ".format(name))

my_fnc2("홍길동")

# 여러 개의 인자를 전달받는 함수
def contact(name, phone, email, addr):
    print("이름 : {}".format(name))
    print("연락처 : {}".format(phone))
    print("이메일 : {}".format(email))
    print("주소 : {}".format(addr))

contact("홍길동", "010-000-000", "tued@naver.com", "경기")

# 인자가 있고, 리턴값도 있는 함수
def fnc_return(name, addr):
    print("이름 : {} ".format(name))
    return name + addr

member = fnc_return("홍길동", "서울")
print(member)

# 두 개값을 리턴 하는 함수
def fnc_multi_return(id, pw):
    print("아이디 {}".format(id))
    print("비밀번호 {}".format(pw))
    return id, pw

(rID, rPW) = fnc_multi_return("test", "1234")
print("아이디 {0} / 비밀번호 {1}".format(rID, rPW))

# 리스트를 전달받는 함수
def fnc_list(listData):
    print("**********")
    print("listData[0] : {}".format(listData[0]))
    print("listData[1] : {}".format(listData[1]))
    print("listData[2] : {}".format(listData[2]))
    print("**********")

listData = ["이름", "010", "서울"]
fnc_list(listData)

fnc_list(["이름", "010", "서울"])

# 반복 횟수를 전달 받는 함수 
def fnc_for(n):
    for k in range(n):
        print("test")

fnc_for(1)
fnc_for(5)

# 아무일도 하지 않는 함수
def fnc_pass():
    pass

fnc_pass()

### 함수의 인자(매개변수) 및 함수내의 변수는 함수 종료후 자동 소멸
def fnc_variable(n1, n2):
    sum = n1 + n2
    print(sum)

fnc_variable(10, 30)
'''
함수 내에 생성된 변수이기 때문에 외부에서 접근 불가능!!!!
print(n1)
print(n2)
print(sum)
'''
"""
파이썬 파일 내에 선언한 변수 : 전역변수
함수 내에 선언한 변수 : 지역변수
"""

var_global = 10

def fnc1():
    var_fnc1 = 15
    print("fnc1 함수 내의 var_fnc1 지역 변수 : {}".format(var_fnc1))
    

def fnc2():
    var_global = 150
    print("fnc1 함수 내의 var_global 지역 변수 : {}".format(var_global))
 

def fnc3():
    global var_global
    var_global= 0
    print(" var_global 전역 변수 : {}".format(var_global))


print(var_global)
fnc1()
fnc2()
fnc3()
print(var_global)

# 1. 람다 함수를 직접 선언 하여 사용하는 방법
(lambda x : x**3) (3)

# 2. 람다 함수 선언을 변수에 저장하여 사용하는 방법 (일반적으로 사용하는 방법)
square = lambda x : x**2
square(3)
square(4)
square(77)

square2 = lambda x, y, z : x**2+y-z
square2 (3, 4, 5)


### 내장함수 : 형변환 함수

# 1. 정수 형변환  : int()
int_list = [int(0.22), int(3.222), int(-23.44)]
print(int_list)

int_list2 = [int('2'), int('3222'), int('-23')]
print(int_list2)



# 2. 실수 형변환 : float()
float_list = [float(23), float(-2233), float(0)]
print(float_list)

float_list2 = [float('23.2'), float('-2233.55'), float('11')]
print(float_list2)

# int() / float() 오류 발생
err_list = [int('10_'), float('12.33a')]
# => ValueError: invalid literal for int() with base 10: '10_'


#  3. 문자 형변환 : str() 은 주로 숫자를 문자로 변경 시 사용
str_list = [str(222), str(12.33), str(-234), str(-0.2222)]
print(str_list)


#  4. 자료구조 형변환 : list() / tuple() / set()
list_data = ['cccc', 12, 112, 'test']
tuple_data = ('cccc', 12, 112, 'test')
set_data = {'cccc', 12, 112, 'test'}

type_test_list = [type(list_data), type(tuple_data), type(set_data)]
print(type_test_list)


# tuple_data 와 set_data 를 리스트 타입으로 형변환
print("리스트로 변환", list(tuple_data), list(set_data))
# => ['cccc', 12, 112, 'test'] ['cccc', 'test', 112, 12]

# list_data 와 set_data 를 튜플 타입으로 형변환
print("튜플로 변환", tuple(list_data), tuple(set_data))
# => ('cccc', 12, 112, 'test') ('cccc', 'test', 112, 12)

# list_data 와 tuple_data 를 셋 타입으로 형변환
print("셋으로 변환", set(list_data), set(tuple_data))
# => {'cccc', 'test', 12, 112} {'cccc', 'test', 12, 112}


###  5. bool 함수 : bool() => True / False ###

# 숫자 : 0 일 경우 => False , 그외의 숫자는 모두 True
print(bool(0))         #  False
print(bool(1))
print(bool(110))
print(bool(-1110))
print(bool(0.22))
print(bool(-2.3303))


# 문자열 : 문자가 있으면 True, 문자가 없으면 False
print(bool('a'))   # True
print(bool(''))
print(bool(' '))   # True
print(bool(None))


# 리스트 / 튜플 / 셋 : 데이터 존재 시 True, 없으면 False
empty_list = []     # False
empty_tuple = ()
empty_set = {}

list_item = [1,2,3]      # True
tuple_item = (2, 3, 4)
set_item = {10, 22, 33}

print(bool(empty_list))
print(bool(empty_tuple))
print(bool(empty_set))

print(bool(list_item))
print(bool(tuple_item))
print(bool(set_item))


### bool() 함수 활용의 예
def prn_name(name):
    if bool(name):
        print("입력된 이름 : ", name)
    else:
        print("입력된 이름이 없습니다")

prn_name("홍길동")

prn_name("")


### 내장 함수 :  기타 집계 함수 및 수학관련 함수
### 숫자에 관련된 함수는 Numpy 라는 별도의 라이브러리로 제공
 
# 최대값 : max()  / 최소값 : min()
num_list = [10, 3, 21, 0.1, 3.5, 44, 33]
print(max(num_list), min(num_list))

str_data ="zsqayt"
print(max(str_data), min(str_data))

num_tuple = (10, 3, 21, 0.1, 3.5, 44, 33)
print(max(num_tuple), min(num_tuple))

num_set = {10, 3, 21, 0.1, 3.5, 44, 33}
print(max(num_set), min(num_set))


# 합 : sum() /  갯수 : len()
print(sum(num_list))
print(sum(num_tuple))
print(sum(num_set))

print(len(num_list))
print(len(num_tuple))
print(len(num_set))


# 절대값 : abs()
abs_list = [-1.23, -123, 234, 456]

print(abs(abs_list[0]))
print(abs(abs_list[1]))
print(abs(abs_list[2]))
print(abs(abs_list[3]))


# 유니코드 값을 문자로 반환 : chr()
# => 눌려진 키보드 값을 문자로 변환 시 자주 사용
code_num1 = 97
code_num2 = 65

print(chr(code_num1))   # a
print(chr(code_num2))   # A


#  리스트, 튜플, 문자열 들을 열거형으로 반환 : enumerate()
stock_list = ['Naver', 'Kakao', 'SK']

for idx, stock in enumerate(stock_list):
    print(idx, stock)


#  입력된 값을 정렬한 후, 리스트로 반환 : sorted()
raw_list = [4, 2, 1, 7, 9, 10]
sorted_list = sorted(raw_list)   # [1, 2, 4, 7, 9, 10]

print(sorted_list)  

import stock

print(stock.author)

upper = stock.cal_upper(10000)
print(upper)

lower = stock.cal_lower(10000)
print(lower)

# 시간에 관련된 모듈
import time

# time.time() : 현재 날짜 및 시간을 1970.1.1 00:00:00 부터 
# 계산하여 숫자로 반환하는 함수
print(time.time())

# time.ctime() 현재 날짜 및 시간을 문자열로 반환하는 함수
print(time.ctime())

current_time = time.ctime()

# split(' ') 설정한 구분 값을 이용하여 
# 문자열을 분리하여 리스트로 반환하는 함수
print(current_time.split(' '))


# time.sleep(1) 설정한 시간동안 대기하는 함수 : 초 단위
for t in range(10):
    print(t)
    time.sleep(1)

# 모듈 내부의 변수, 함수를 확인하는 방법 : dir(모듈명)
dir(time)

# 유용한 운영체제 관련 모듈 : os
import os

# os.getcwd() : 현재 작업 폴더 경로
print(os.getcwd())

# os.listdir() : 현재 작업 폴더 내의 파일 목록
print(os.listdir())

# os.listdir('C:/Anaconda3') : 특정 폴더내의 파일 목록을 리스트로 반환
files = os.listdir('C:/Anaconda3')
print(len(files))

print(type(files))

# x.endswith('exe') : 확장자가 'exe'인 지 확인
for x in files:
    if x.endswith('exe'):
        print(x)



# 모듈 import하는 방법

# 1. import 모듈명
import os
dir()

# 2. from  모듈명 import 함수명
from os import listdir
dir()

# 3. import 모듈명 as 단축이름
# => 모듈명이 길 경우, 이름을 별도로 설정
import os as winos
path_str = winos.getcwd()
print(path_str)

#####################################
# 클래스 선언
class Bicycle():
    pass

# 선언된 클래스를 이용한 객체 생성
bicycle1 = Bicycle()
print(bicycle1)  # <__main__.Bicycle object at 0x00000251327B4430

'''
__main__   모듈 자기 자신
0x  16진수 
00000251327B4430  생성된 객체의 메모리 번지
'''

class Card:
    def set_info(self, name, email):
        self.name = name
        self.email = email


member = Card()
member    # <__main__.Card at 0x251327b49a0>

member.set_info("홍길동", "hong@h.com")
print(member.name)
print(member.email)

## self 는 생성된 객체 자기 자신을 뜻함!!!!!!
'''
따라서   name, email 과 self.name, self.email 는 다른 변수
         elf.name, self.email 는 객체 변수 
'''

# 클래스 선언 : 생성자 / 소멸자 / 클래스 변수 / 인스턴스 변수
class Bicycle():
    
    # 클래스 변수 선언
    instance_count = 0
    
    # 생성자 선언
    def __init__(self, wheel_size, color):
        print("객체생성")
        # 인스턴스 변수 선언
        self.wheel_size = wheel_size
        self.color = color
    
    # 인스턴스 메서드 선언
    def move(self, speed):
        print("자전거 시속 {} km".format(speed))
        
    # 인스턴스 메서드 선언
    def turn(self, direction):
        print("자전거 : {}".format(direction))

    # 인스턴스 메서드 선언
    def stop(self):
        print("자전거 {0}, {1} : 정지".format(self.wheel_size, self.color))
        
    # 정적 메서드 선언
    @staticmethod
    def check_type(model_code):    
        print("정적 메서드 호출")
        
    # 클래스 메서드 선언
    @classmethod
    def count_instance(cls):
        print("객체의 갯수 {}".format(cls.instance_count))
        
    # 소멸자 선언
    def __del__(self):
        print("객체 소멸")

# 클래스 변수 호출
print(Bicycle.instance_count)

# 클래스 객체 생성 
obj1 = Bicycle(20, 'white')

# 인스턴스 변수 호출
print(obj1.wheel_size, obj1.color)

# 인스턴스 메서드 호출
obj1.move(100)
obj1.turn("left")
obj1.stop()

# 정적 메서드 호출
Bicycle.check_type('Classic')

# 클래스 메서드 호출
Bicycle.count_instance()

########  파이썬 클래스 상속  ######
class Child(Bicycle):
    
    def __init__(self):
        Bicycle.__init__(10, 'yellow')

child = Child()

# 상속 메서드 호출
child.stop()



class Test:
    def __init__(self):
       print("객체 생성")
        
    def __del__(self):
       print("객체 소멸")

test = Test()






















