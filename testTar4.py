# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:10:21 2020

@author: hagit
מספר ראשוני הוא מספר שלם המתחלק רק ב-1 ובעצמו. כתוב פונקציה isprime
המקבלת כקלט מספר שלם n ומחזירה True אם הוא ראשוני ו-False אחרת.

ב-script ראשי בקש מהמשתמש להזין מספר שלם חיובי num) אם לא חיובי, הצג
הודעה וסיים). תוך שימוש בפונקציה isprime הצג:
האם num הוא ראשוני או לא
כמה מספרים ראשוניים יש בין 1 לבין המספר num) כולל num ,ללא קשר אם
num עצמו הוא ראשוני)

str(num) + " 
    הצג שתי דוגמאות הרצה בלתי תלויות עבור: 11 =num ,12 =num
"""

# Count primes function
def count_Primes(num):
    ctr = 0   
    for num in range(num):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr

# Is it a prime number function
def isprime(num): 
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               return(str(num) + " is not a prime number" +
                      "\n" + " There are " + str(count_Primes(num)) + 
                      "\n" + "Prime numbers between 1 and " + str(num))      
               break
       else:
           return(str(num) + " is a prime number"+
                      "\n" + " There are " + str(count_Primes(num)) + 
                      "\n" + "Prime numbers between 1 and " + str(num))
    else:
       return(str(num) + " is not a prime number"+
                      "\n" + " There are " + str(count_Primes(num)) + 
                      "\n" + "Prime numbers between 1 and " + str(num))

# Gets number and check if it's a prime number and how many primes came before
num =int(input('Please enter a positive number: '))
if num>0:
    print(isprime(num))
else:
    print("You have entered a negative number - Finished")
    
    
    
    
    
    