# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:08:13 2021

@author: Playdata

contact_5_menu3_remove.py
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

# 사용자로부터 입력 받기 : 메뉴 1
def set_contact():
    name = input("이름 :")
    phone_number = input("연락처 :")
    e_mail = input("이메일 :")
    addr = input("주소 :")
    # print(name, phone_number, e_mail, addr)
    contact = Contact(name, phone_number, e_mail, addr)
    return contact
# ---- def set_contact(): END----------------

# 사용자 입력내용 출력 : 메뉴 2
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()
# ---- def print_contact(contact_list): END -------


# 이름으로 연락처 삭제 : 메뉴 3
def delete_contact(contact_list, name):
    for idx, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[idx]
# ---- def delete_contact(contact_list, name): END -------


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

# 종료 전에 사용자가 입력한 데이터(contact_list) 를파일로 저장 : 메뉴 4 
def store_contact(contact_list):
    f = open("contact_db.txt", "w")
    
    for contact in contact_list:
        f.write(contact.name + "\n")
        f.write(contact.phone_number + "\n")
        f.write(contact.e_mail + "\n")
        f.write(contact.addr + "\n")
    f.close()
# ----- def store_contact(contact_list): END -----    


# 프로그램 실행 시, 저장된 파일을 로드하여, contact_list에 저장
def load_contact(contact_list):
    f = open("contact_db.txt")
    
    lines = f.readlines()
    num = len(lines)/4
    num = int(num)
    
    for i in range(num):
        name = lines[4*i].rstrip("\n")
        phone = lines[4*i+1].rstrip("\n")
        email = lines[4*i+2].rstrip("\n")
        addr = lines[4*i+3].rstrip("\n")
        
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
        
    f.close()
#------- def load_contact(contact_list): END -------------    
    

# 모듈 자체 실행 시에만 호출됨
def run():
    # Contact 객체들을 저장할 리스트 선언
    contact_list = []
    
    # 저장된 파일 내용으로 contact_list 에 채우기
    load_contact(contact_list)
    
    while 1:
        menu = print_menu()
        
        if menu == 1:
            contact =  set_contact()        # 사용자 입력화면 출력 및 결과 저장
            contact_list.append(contact)    # 저장된 contact 객체를 리스트에 추가 
        
        elif menu == 2:
            print_contact(contact_list)
            
        elif menu == 3:
            name = input("Delete Name :")
            delete_contact(contact_list, name)
            
        elif menu == 4:
            store_contact(contact_list)
            break

# 모듈 자체 실행인지, import에 의해 실행인지를 구분
if __name__ == "__main__":
    run()
    
#   









