# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:01:12 2021

@author: Playdata  

File name : stock.py
"""
def cal_upper(price):
    increment = price * 3
    upper_price = price + increment
    return upper_price

def cal_lower(price):
    decrement = price * 0.3
    lower_price = price - decrement
    return lower_price

author = "testStock"
