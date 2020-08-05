# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:25:35 2020

"""

# Recur factorial function
def recur_factorial(num):
   if num == 1:
       return num
   else:
       return num*recur_factorial(num-1)

# Function sum mult
def mult_sum(num, op):
    try:
        int(op)
    except:
        op=1
    op = int(op)
    if op==2:
        return ("Mult is : " + str(recur_factorial(num)))
    else:    
         my_sum = 0
         i=0
         while i <= num:
            my_sum = my_sum + i
            i+=1
         return ("Sum is : " + str(my_sum))

# Gets inputs from the user to the function
num =int(input('Please enter a positive number: '))
print("Options : " + "\n" + "1. Sum"  + "\n" + "2. Mult")
op =(input('Please choose an option: '))
print(str(mult_sum(num, op)))















