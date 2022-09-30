# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:52:00 2021

@author: Raisa
"""

p=int(input("enter value p:"))
q=int(input("enter value q:"))
try:
        r=p/q
        print("res:",r)
except ZeroDivisionError:
        print("cannot be divided by zero")
except ValueError as arg:
        print("error:",arg)
finally:
        print("this is always executed")
