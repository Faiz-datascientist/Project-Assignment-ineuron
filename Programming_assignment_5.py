#!/usr/bin/env python
# coding: utf-8

# # 1. Write a Python Program to Find LCM?

# In[10]:


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

num1 = 12
num2 = 14

print("The L.C.M. is", lcm(num1, num2))


# # 2. Write a Python Program to Find HCF?

# In[9]:


def findTheHcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if((x%i == 0) and (y%i == 0)):
            hcf = i
    print(f'The HCF of {x},{y} is {hcf}')

findTheHcf(12,14)
findTheHcf(4,7)
findTheHcf(10,23)


# # 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

# In[11]:


def DecimalToOther():
    num = int(input('Enter a Number: '))
    print(f'Binary Number -> {bin(num)}')
    print(f'Octal Number -> {oct(num)}')    
    print(f'Hexadecimal Number -> {hex(num)}')    

DecimalToOther()


# # 4. Write a Python Program To Find ASCII value of a character?

# In[12]:


def charToAscii():
    char = input('Enter a Character: ')
    if len(char) > 1:
        print('Please Enter a Single Character')
    else:
        print(f'Ascii Character of {char} is {ord(char)}')

charToAscii()


# # 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[ ]:



import operator

ops = { "+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.truediv } 

print('Select a Arithmetic Operation:         \n1.Addition(+)        \n2.Division(-)        \n2.Multiplication(*)        \n4.Division(/)        \n3.Stop(0)\n')
   

while True:
    operator = input('Enter a arithmetic operation -> ')
    if operator == '0':
        print("Program Stopped successfully")
        break
    elif operator not in ['+','-','*','/']:
        print("Please enter a valid operator")
    else:
        num_1 = int(input('\nEnter 1st Number: '))
        num_2 = int(input('Enter 2nd Number: '))
        print(f'{num_1}{operator}{num_2}={ops[operator](num_1,num_2)}\n')


# In[ ]:




