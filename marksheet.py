# -*- coding: utf-8 -*-
"""marksheet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pTMar7MCbEGgQgOQ8uxsKVDHZ5xKMqb3
"""



name=input("enter your name:  ")
maths=int(input("Enter marks of the maths: "))
english=int(input("Enter marks of the english: "))
chem=int(input("Enter marks of the chem: "))
phy=int(input("Enter marks of the physics: "))
computer=int(input("Enter marks of the computer: "))
print("Name : ",name)

print('-----------------------------------')
print("English  \t\t\t\t", english)
print('-----------------------------------')
print("Maths \t\t\t\t\t", maths)
print('-----------------------------------')
print("chemistry  \t\t\t\t", chem)
print('-----------------------------------')
print("physics  \t\t\t\t", phy)
print('-----------------------------------')
print("computer  \t\t\t\t", computer)
print('-----------------------------------')


total=(maths+english+chem+phy+computer)
print('your total markes is ',total)
percentage=total/500*100
print('your percentage is',percentage)
if(percentage>=90):
    print("Grade: A")
elif(percentage>=80&percentage<90):
    print("Grade: B")
elif(percentage>=70&percentage<80):
    print("Grade: C")
elif(percentage>=60&percentage<70):
    print("Grade: D")
else:
    print("Grade: F")

 