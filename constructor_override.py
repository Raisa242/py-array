# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 11:15:12 2021

@author: Raisa
"""

class base:
    def __init__(self):
        self.s="base class method"
    def Amethod(self):
        print(self.s)
        
class derived(base):
    def __init__(self):
        super().__init__()
        self.x="derived class method"
    def Bmethod(self):
        print(self.x)
        
derived().Amethod()
derived().Bmethod()