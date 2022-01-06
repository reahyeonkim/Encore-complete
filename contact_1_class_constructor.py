# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:08:13 2021

@author: Playdata

contact_1_class_constructor.py
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


# 모듈 자체 실행 시에만 호출됨
def run():
    test = Contact("홍길동", "010-5555-4444", "test@test.com", "서울")
    test.print_info()

# 모듈 자체 실행인지, import에 의해 실행인지를 구분
if __name__ == "__main__":
    run()
    
#   