# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 18:16:18 2020

@author: hagit

בנה רשימה (list (המכילה את כל המספרים השלמים בין 1 ל-100 המתחלקים
בלפחות אחד המספרים הבאים: ב-6 ,ב-15 ,ב-35.
הצג בליווי הודעה מתאימה:
מיהם המספרים האלה (את המספרים הצג כרשימה)
כמה מספרים כאלה יש בסה"כ
בנה מהרשימה שנוצרה שתי רשימות חדשות: אחת המכילה את המספרים
הזוגיים והשנייה את המספרים האי זוגיים. הדפס כל רשימה ולידה כמה
מספרים זוגיים/אי זוגיים בהתאמה
"""

# Code section
my_num_list = []
i = 0
i = int(i)
for d in range(100):
    i = i + 1
    if (i % 6 == 0 or i % 15 == 0 or i % 35 == 0):
        my_num_list.append(i)

# First list        
print("First list : " + "\n" +
      str(my_num_list))
print("The list contains " + str(len(my_num_list)) + " numbers")

# Sub lists definition and creation
dual_num_list = []
odd_num_list = []
b = 0
for z in range(len(my_num_list)):
    if (my_num_list[b]%2==0):
        dual_num_list.append(my_num_list[b])
    else:
        odd_num_list.append(my_num_list[b])
    b = b + 1    
    
# Prints lists   
print("Dual numbers list : " + "\n" +
      str(dual_num_list))
print("The list contains " + str(len(dual_num_list)) + " numbers")
print("Odd numbers list : " + "\n" +
      str(odd_num_list))
print("The list contains " + str(len(odd_num_list)) + " numbers")










