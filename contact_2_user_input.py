# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:08:13 2021

@author: Playdata

contact_2_user_input.py
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

# 사용자로투터 입력 받기
def set_contact():
    name = input("이름 :")
    phone_number = input("연락처 :")
    e_mail = input("이메일 :")
    addr = input("주소 :")
    print(name, phone_number, e_mail, addr)

# 모듈 자체 실행 시에만 호출됨
def run():
    set_contact()

# 모듈 자체 실행인지, import에 의해 실행인지를 구분
if __name__ == "__main__":
    run()
    
#   