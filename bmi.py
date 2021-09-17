# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:38:02 2021

@author: Anutua
"""
"""Minister request"""

def bmi(h,w):
    height=float(h)
    weight=float(w)
    bmi=weight/(height**2)
    return bmi

userheight=input('Enter your height in metres:')
userweight=input('Enter your weight in kg:')

userbmi=bmi(userheight,userweight)
print('Your bmi is', userbmi)

 