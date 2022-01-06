# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:08:13 2021

@author: Playdata

contact_3_menu4_exit.py
"""
#### Contact 클래스 선언 ####
class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
        
    def print_info(self):
        print("Name : ", self.name)
        print("Phone Number : ", self.phone_number)
        print("E-mail : ", self.e_mail)
        print("Address : ", self.addr)

#### class Contact END ####

# 사용자로부터 입력 받기
def set_contact():
    name = input("이름 :")
    phone_number = input("연락처 :")
    e_mail = input("이메일 :")
    addr = input("주소 :")
    print(name, phone_number, e_mail, addr)
# ---- def set_contact(): END----------------

# 메인 메뉴 구성
# 1. 입력 / 2. 출력 / 3. 삭제 / 4. 종료
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴 선택 :")

    return int(menu)
# ---- def print_menu(): END ---------


# 모듈 자체 실행 시에만 호출됨
def run():
    while 1:
        menu = print_menu()
        
        if menu == 4:
            break

# 모듈 자체 실행인지, import에 의해 실행인지를 구분
if __name__ == "__main__":
    run()
    
#   