""""
Date : 16.03.2022
Prepared by the Program : Hasan
Name Of The Program : Detects email addresses without email domains in a text
###################################################

Write a program that list according to email addresses without email domains in a text.
Example:
Input:
The advencements in biomarine studies franky@google.com with the investments necessary 
and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...

Output :
franky
sinatra123
"""
#####################################################################
import re
try : 
    sentence=input("Enter the sentence : ")
    patern=r"(\w{0,})@(\w{0,})"

    for i in re.finditer(patern,sentence):    
        print(i.groups()[0])
        
except:
    print("Mail adress not found...")
#####################################################################