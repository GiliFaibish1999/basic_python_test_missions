# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:55:06 2020

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






























