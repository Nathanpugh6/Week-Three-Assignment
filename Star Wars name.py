# Nathan Pugh
# CIS 125 82A
# Week 3 Lab
# 23 September 2015

# Create Variables for the components of the whole Star Wars name

First = input("What is your first name: ") 
Last = input("What is your last name: ")
Mother = input("What is your mother's maiden name: ")
Town = input("What is the name of your town of birth: ")

FirstThree = Last[:3] #goes through the first 3
FirstTwo = First[:2] #goes through the first 2
LastTwo = Mother[:2] #goes through first 2
LastThree = Town[:3] #goes through the first 3

FirstName = FirstThree + FirstTwo #creates first name
LastName = LastTwo + LastThree #creates last name

print(FirstName.capitalize(), LastName.capitalize()) 