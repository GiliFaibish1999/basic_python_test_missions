# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:55:06 2020

@author: hagit
סטודנט מושלם הוא סטודנט שציוניו בכל המטלות בקורס מראות על עליה בציון או
לפחות אי ירידה בציון בין מטלה למטלה.
כתוב פונקציה mushlam המקבלת כקלט list של מספרים שלמים ומחזירה True אם
רצף המספרים מקיים את התנאי של מושלם. אחרת תחזיר False .

ב-script ראשי קלוט מהמשתמש לתוך רשימה 4 ציונים (הנח שהקלט תקין) והצג
הודעה האם הסטודנט מושלם או לא.

הצג שתי דוגמאות הרצה בלתי תלויות עבור שני הצירופים הבאים של ציונים (משמאל
לימין):
88, 86, 94, 99
93, 97, 98, 100 
"""
# Is it a perfect student function
def mushlam(gradesList): 
    for i in range( len(gradesList) - 1 ):
        if gradesList[i] < gradesList[i+1]:
            return True
        return False

# Gets grades list and check if the student is perfect or not
input_grades = input("Enter the list of 4 grades separated by commas : ")
print("\n")
gradesList = input_grades.split(",")
print("Perfect student : " + str(mushlam(gradesList)))






























