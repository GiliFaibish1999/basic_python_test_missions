# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:25:35 2020

@author: hagit
כתוב פונקציה (op, n(mult_sum המקבלת מספר חיובי ושלם n וכן פרמטר op .אם
‘sum=’op הפונקציה מחזירה את סכום המספרים מ-1 עד וכולל n .אם ‘mult=’op
הפונקציה מחזירה את מכפלת המספרים מ-1 עד וכולל n .ברירת המחדל של op היא
 .‘sum’

ב-script ראשי קלוט מהמשתמש מספר חיובי ושלם וכן אינדיקציה אם sum או mult
(הנח שהקלטים תקינים). תוך שימוש בפונקציה (op, n(mult_sum ובליווי הודעה
מתאימה הצג את התוצאה עבור הקלטים.

הצג שתי דוגמאות הרצה בלתי תלויות עבור הקלטים הבאים:
5, sum
6, mult
הצג דוגמת הרצה נוספת עבור 7=n בה op נקרא עם ברירת מחדל 
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















