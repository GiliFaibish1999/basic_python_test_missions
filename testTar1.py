
# Imports
import re

# Code section

# Base sentence
my_sentence= "Good luck in the exam"

# Prints sentence length
print("Sentence length is " + str(len(my_sentence)) + " chars")

# Prints the number of time the letter 'a' appears
regex = 'a'
match = re.findall(regex, my_sentence)
print("The letter 'a' appears " + str(len(match)) + " times")

# Prints if the combination 'xa' appears or not
regex_2 = 'xa'
match_2 = re.findall(regex_2, my_sentence)
if len(match_2)>0:
    print("The combination 'xa' appears in the sentence")
else: 
    print("The combination 'xa' does not appear in the sentence")    
    
# Prints a list of the chars in the odd spots    
list_my_sentence = list(my_sentence)   
list_my_sentence_odd =[]
i = 0
for z in range(len(list_my_sentence)):
    if (i%2==0):
        pass
    else:
        list_my_sentence_odd.append(list_my_sentence[i])
    i = i + 1    
print("Odd spots list : " + str(list_my_sentence_odd))

    
    
    
    
    
    
    
    
    
    
    
