""""
Date : 16.03.2022
Prepared by the Program : Hasan
Name Of The Program : Detects the ID number
###################################################

The format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 
1 letter, 1 digit (For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6
Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678
Output : VZ4PF94B6

"""
#####################################################################
import re
try : 
    text=input("Enter a text : ")
    patern=r'\w{2}\d\w{2}\d{2}\w\d'
    id=re.search(patern,text)
    print("Id Number is : ",id[0])
except:
    print("ID number not found...")
#####################################################################
