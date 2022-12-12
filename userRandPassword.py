"""
This python code generates random passwords for users. 
The password is 12 characters at least

"""

import random, math

#A set that contains all possible values i.e alpahnumeric and symbols
rand_lst = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/?.>,<"|#$%^&*()' 
size_of_password = 12   
gen_pass = ""
lenght = len(rand_lst)

for x in range(size_of_password):
    gen_pass += rand_lst[math.floor(random.random() * lenght)]
   

y_name = input('Enter Your Name Here: ') 

def credentials(password=gen_pass):
    username = y_name
    print(f'Hello {username} , your password is {password}')

credentials()
