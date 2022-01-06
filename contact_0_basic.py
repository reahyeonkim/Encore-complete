# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:08:13 2021

@author: Playdata

contact_0_basic.py
"""
# 기본 코드 
def run():
    print("Contact")


# __name__ : 모듈 자체가 실행되면 '__main__' 이라는 문자열을 보유
# 따라서 __name__  이 어떤 문자열을 보유 하고 있는 지에 따라
# 모듈 자체가 실행되고 있는 지, 다른 파일에 의해 import 되어 실행되고 
# 있는지를 확인할 수 있다.
if __name__ == "__main__":
    run()
    
#   