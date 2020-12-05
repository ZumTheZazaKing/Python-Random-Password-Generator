#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 23:13:51 2020

@author: muhammadzahidi
"""
import time
import random
import string

print('-'*70)

print('                       Random Password Generator')

def main():
    
    print('-'*70)
    
    time.sleep(2)
    
    password_length = int(input("""How long would you like your password to be?\n
Please tell me in numbers and don't go over 16:"""))


    print('-'*70)
    
    print('Processing...')
    
    print('-'*70)
    
    time.sleep(3)
    
    password_characters = string.ascii_letters + string.digits + string.punctuation
    
    password = []
    
    for x in range(password_length):
        
        password.append(random.choice(password_characters))
        
    password = ''.join(password)
    
    print('Your newly generated password is ' + password)
    
    
while True:
    
    main()
    
    time.sleep(2)
    
    if str(input("""Would you like to generate another one?(Y/N)""")).strip().upper() != 'Y':
        
        print('\nGoodbye!\n')
        
        time.sleep(2)
        
        break
    
    
    