# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:37:51 2020

@author: Sahar
"""
#maximum between 3 different number:

def max_num (num1, num2, num3):
 
    if num1 >= num2 and num1 >= num3 :
        
    #if num1 > num2 & num3, choose num1         
        return num1
    
    #elseif num2> num1 & num3, choose num2 
    elif num2 >= num1 and num2 >= num3 :
        
     return num2
 
    #else choose num3
    else:
     
     return num3
 
    
#take two number and find the square
def func1(x,y):
    return  (x+y) ** (x+y)

    

