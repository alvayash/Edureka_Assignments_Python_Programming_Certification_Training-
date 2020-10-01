'''
Module 3–Deep Dive -Functions, OOPs, Modules, Errors and Exceptions

Case Study

1. A Robot moves in a Plane starting from the origin point (0,0). The robot can move
toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after directions are steps.  Write a program to compute the distance current position after sequence of movements.
Hint: Use math module.
'''

print('Answer for Question 1 Begins ')

import math

v_origin_x=0
v_origin_y=0
v_new_x_coordinate=0
v_new_y_coordinate=0

v_up=1
v_down=-1
v_left=-1
v_right=1

v_up_counter=0
v_down_counter=0
v_left_counter=0
v_right_counter=0

while True:
    print('Enter where your Robot wants to go :')
    print('1. Enter U for UP ')
    print('2. Enter D for DOWN ')
    print('3. Enter L for LEFT ')
    print('4. Enter R for RIGHT ')
    print('5. Enter S to STOP')
    user_input = str(input('Enter your input : '))
    if user_input.upper()=='S':
        break
    else:
        if user_input.upper()=='U':
            v_up_counter+=1
        elif user_input.upper()=='D':
            v_down_counter+=1
        elif user_input.upper()=='L':
            v_left_counter+=1
        elif user_input.upper()=='R':
            v_right_counter+=1

v_up_counter=v_up_counter*v_up
v_down_counter=v_down_counter*v_down
v_left_counter=v_left_counter*v_left
v_right_counter=v_right_counter*v_right

v_new_x_coordinate=v_left_counter+v_right_counter
v_new_y_coordinate=v_up_counter+v_down_counter

v_distance_formula=math.sqrt((v_new_x_coordinate-v_origin_x)**2+(v_new_y_coordinate-v_origin_y)**2)

print('Current X Co-ordinate of ROBOT is :',v_new_x_coordinate)
print('Current Y Co-ordinate of ROBOT is :',v_new_y_coordinate)
print('Distance of the ROBOT from Origin is :',v_distance_formula)
print('\n')


'''
2.
Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.
Hint:
Use if/elif to deal with conditions.
'''
print('Answer for Question 2 Begins ')

import json
# Opening file
f=open('Expense.json')

# returns JSON object as a dictionary
data = json.load(f)

# Closing file
f.close()

emp_details = data['emp_details']

# Iterating through the json
# list
for i in emp_details:
    print(i)


emp_name = emp_details[0]['WHO']
emp_week = emp_details[0]['WEEK'][2]

print(emp_name,emp_week)

print('Welcome to XYZ Company')
print('Following are the list of Employees, who are currently working with us :\n')
print(' 1.Joe \n 2.Beth \n 3.Janet \n')
user_input_emp=str(input('Enter name of Employee you want to view Details :'))

if user_input_emp.upper()=='JOE':
    addional_input_1=int(input('Which week information do you want to view ( 3,4,5 ):'))
    if addional_input_1==3:
        print(emp_details[0]['WEEK'][0])
    elif addional_input_1==4:
        print(emp_details[0]['WEEK'][1])
    elif addional_input_1==5:
        print(emp_details[0]['WEEK'][2])
    else:
        print('Input Week for employee JOE not found.')
elif user_input_emp.upper()=='BETH':
    addional_input_1=int(input('Which week information do you want to view ( 3,4,5 ):'))
    if addional_input_1==3:
        print(emp_details[1]['WEEK'][0])
    elif addional_input_1==4:
        print(emp_details[1]['WEEK'][1])
    elif addional_input_1==5:
        print(emp_details[1]['WEEK'][2])
    else:
        print('Input Week for employee BETH not found.')
elif user_input_emp.upper()=='JANET':
    addional_input_1=int(input('Which week information do you want to view ( 3,4,5 ):'))
    if addional_input_1==3:
        print(emp_details[2]['WEEK'][0])
    elif addional_input_1==4:
        print(emp_details[2]['WEEK'][1])
    elif addional_input_1==5:
        print(emp_details[2]['WEEK'][2])
    else:
        print('Input Week for employee JANET not found.')
else:
    print('Input User not found')

print('\n')


'''
3.
Weather forecasting organization wants to show is it day or night. So, write a program for such organization to find whether is it dark outside or not.
Hint: Use time module.
'''
print('Answer for Question 3 Begins ')

import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

print('Current Time is :',current_time)
if current_time>'18:29:00':
    print('Yes, It is Dark Outside')
else:
    print('No, It is not Dark Outside')

print('\n')

'''
4.
Write a program to find distance between two locations when their latitude and longitudes are given.
Hint: Use math module.
'''

print('Answer for Question 4 Begins ')

from math import radians, sin, cos, acos

print("Input coordinates of two points:")
slat = radians(float(input("Starting latitude: ")))
slon = radians(float(input("Ending longitude: ")))
elat = radians(float(input("Starting latitude: ")))
elon = radians(float(input("Ending longitude: ")))

dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
print("The distance is %.2fkm." % dist)
print('\n')

'''
5.
Design a software for bank system. There should be options like cash withdraw, cash credit and change password.
According to user input, the software should provide required output.
Hint: Use if else statements and functions.
'''

print('Answer for Question 5 Begins ')

account_balance=100000
current_password='Abc@123'

def cash_withdraw(account_balance,withdraw_amount):
    if withdraw_amount>=account_balance:
        print('Insufficient Balance')
    else:
        account_balance=account_balance-withdraw_amount
        print('Withdrawal Amount of ',withdraw_amount,'successful ')
        print('Current Account Balance is ',account_balance)
    return account_balance

def cash_credit(account_balance,credit_amount):
        account_balance=account_balance+credit_amount
        print('Credit Amount of ',credit_amount,'successful ')
        print('Current Account Balance is ',account_balance)
        return account_balance

try:
    while True:
        print('Welcome to ABC Bank')
        print(' 1. Cash Withdraw \n 2. Cash Credit \n 3. Change password \n 4. Exit')
        user_option = int(input('Please select any one option to continue :'))
        if user_option == 1:
            print('Your current account_balance is :',account_balance)
            user_withdrawal_amount = int(input('Please enter the amount to be withdrawn :'))
            account_balance = cash_withdraw(account_balance, user_withdrawal_amount)
            break
        elif user_option == 2:
            print('Your current account_balance is :', account_balance)
            user_credit_amount = int(input('Please enter the amount to be credited :'))
            account_balance = cash_credit(account_balance, user_credit_amount)
            break
        elif user_option == 3:
            user_current_password=str(input('Please enter your current password : '))
            if user_current_password==current_password:
                new_password=str(input('Please enter new password : '))
                current_password=new_password
                print('Password has been successfully changed')
                break
            else:
                print('Entered password does not match Old password')
                break
        elif user_option == 4:
            break
        else:
            print('Wrong option selected')
            break
except:
    print('Wrong Input')
finally:
    print('Thank you for banking with us')

print('\n')

'''
6.
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

print('Answer for Question 6 Begins ')

list_5_7_combination= []
for i in range(1999,3200):
    if i%5!=0 and i%7==0:
        list_5_7_combination.append(i)

for i in range(len(list_5_7_combination)):
    print(list_5_7_combination[i], end =",")

print('\n')

'''
7.
Write a program which can compute the factorial of a given numbers. Use recursion  to find it.
Hint: Suppose the following input is supplied to the program: 8
Then, the output should be: 40320
'''

print('Answer for Question 7 Begins ')

factorial_result=1
try:
    user_fact_input=int(input('Please enter the number to get factorial :'))
    user_fact_input_copy=user_fact_input

    if user_fact_input==0:
        print('The Factorial of 0 is 1')
    elif user_fact_input==1:
        print('The Factorial of 1 is 1')
    elif user_fact_input<0:
        print('Cannot have Factorial of negative number')
    else:
        while user_fact_input>=1:
            factorial_result=factorial_result*user_fact_input
            user_fact_input-=1
        print('The Factorial of',user_fact_input_copy,'is :',factorial_result)
except:
    print('Wrong input entered')
finally:
    print('Thank you !')

print('\n')

'''
8.
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H: C is 50. H is 30.
D  is  the  variable  whose  values  should  be  input  to  your  program  in  a  comma-separated sequence.
Example:
Let  us  assume  the  following  comma  separated  input  sequence  is  given  to  the program:
100,150,180
The output of the program should be:
18,22,24
'''
print('Answer for Question 8 Begins ')

from math import sqrt

calculated_output=[]

def calculated_func(digit):
    c=50
    h=30
    calculated_output=round(sqrt((2*c*digit)/h))
    return calculated_output

while True:
    try:
        user_math_input_list = [int(x) for x in input("Enter multiple comma separated integer values : \n").split(',')]
        for digit in user_math_input_list:
            calculated_output.append(calculated_func(digit))
        break
    except:
        print('Incorrect input')
        break

print("\nThe values of input are", user_math_input_list)
print("\nThe values of output are", calculated_output)

print('\n')

'''
9.
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the
i-th row and j-th column of the array should be i*j.
Note: i=0,1..,X-1;
      j=0,1..,Y-1.
Example:
Suppose the following inputs are given to the program: 3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''
print('Answer for Question 9 Begins ')

try:
    value_1 = int(input('Enter First Digit : '))
    value_2 = int(input('Enter Second Digit : '))
    final_output_1 = []
    for element in range(0, value_1):
        final_output_2 = []
        for other_element in range(0, value_2):
            final_output_2.append(element * other_element)
        final_output_1.append(final_output_2)
    print('The Output of the 2 dimensional array is : ', final_output_1,'\n')
except:
    print('Incorrect input \n')
finally:
    print('Thank you !')

print('\n')

'''
10.
Write a program that accepts a comma separated sequence of words as input and prints the words
in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

print('Answer for Question 10 Begins ')

user_string_input = [x for x in input("Enter multiple comma separated values : \n").split(',')]
user_string_input.sort()

print('Output of the program is :\n')
print(','.join(user_string_input))

print('\n')

'''
11.
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
print('Answer for Question 11 Begins ')

complete_lines = []
print('Enter Your input : \n')
while True:
    user_line = input()
    if user_line:
        complete_lines.append(user_line.upper())
    else:
        break
final_completed_line = '\n'.join(complete_lines)

print(final_completed_line)
print('\n')

'''
12.
Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''
print('Answer for Question 12 Begins ')

user_seq_input = [x for x in input("Enter multiple whitespace separated values : \n").split(' ')]

user_seq_input=set(user_seq_input)
user_seq_input=list(user_seq_input)
user_seq_input.sort()

print('The output is : ')
for i in range(len(user_seq_input)):
    print(user_seq_input[i], end =" ")

print('\n')

'''
13.
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
'''

print('Answer for Question 13 Begins ')

def binaryToDecimal(n):
    return int(n, 2)

user_binary_input = [x for x in input("Enter multiple comma separated values : \n").split(',')]
try:
    for element in range(len(user_binary_input)):
        decimal_output=binaryToDecimal(user_binary_input[element])
        if decimal_output%5==0:
            print('The binary',user_binary_input[element],'is divisible by 5.')

except:
    print('Entered incorrect input')
finally:
    print('Thank you !')

print('\n')

'''
14.
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program: Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

print('Answer for Question 14 Begins ')

supplied_input = str(input("Enter your sentence : "))
supplied_input_list=[j for j in supplied_input if j.isalpha()==True]
v_is_upper=0
v_is_lower=0

for i in supplied_input_list:
    if i.isupper()==True:
        v_is_upper+=1
    elif i.isupper()==False:
        v_is_lower+=1

print('UPPER CASE :',v_is_upper)
print('LOWER CASE :',v_is_lower)

print('\n')

'''
15.
Give example of fsum and sum function of math library
'''

print('Answer for Question 15 Begins ')

import math

my_tuple = (1, 2.3333, 3.3333, 4.3335, 5)

print('Supplied input :',my_tuple)
print('Output of fsum is :',math.fsum(my_tuple))
print('Output of sum is :',sum(my_tuple))
print('Thank you !')
print('\n')
