# Nathan Pugh
# CIS 125 82A
# Week Three Assignment
# Pig Latin
# 23 September 2015

# The program should prompt the user to enter an English word to translate.

StartingWord = input("What word in English do you wish to translate? ")

# If a word begins with a vowel, append 'yay' to the end of the word.

Vowels = "aeiouAEIOU"
End = "yay"
if StartingWord[0] in Vowels:
    print((StartingWord + End).capitalize())
    
# If a word begins in a consonant, remove the first letter and append it to the end of the word. Finally, append 'ay' to the end of the word.  

else:
    print((StartingWord[1:] + StartingWord[0] + "ay").capitalize())
    
    #I solved the case sensitivity by adding the vowels in both lowercase and uppercase to the variable "Vowels"