# MINI PROJECT_02
"""GENERATE RANDOM PASSWORD"""
import random as rd
import string as str

char_Val = str.ascii_letters + str.digits + str.punctuation
password = ""
for i in range (12):
    password += rd.choice(char_Val)
print(f"Your random password is {password}")