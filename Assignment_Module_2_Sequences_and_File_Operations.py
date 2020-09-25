#  Introduction to Python
## Module 2 - Sequence and File Operations

#####################################################################################################################################

'''
1.
What is the output of the following code?
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))
Hint: Set consists unique element.
'''

print('Answer for Question 1 Begins ')

print('Output is 4 as Set removes duplicates & keeps only unique elements ')
print('\n')

#####################################################################################################################################

'''
2.
What will be the output?
d ={"john":40,"peter":45}
print(list(d.keys()))
Hint:d.keys()is the function which will show keys.
'''
print('Answer for Question 2 Begins ')

print('Output is [''john'', ''peter''] as the Dictionary keys will be converted into a list')
print('\n')

#####################################################################################################################################


'''
3.
A website requires a user to input username and password to register. Write a program 
to check the validity of password given by user. Following are the criteria for checking 
password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12

Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
'''

print('Answer for Question 3 Begins ')

lower_alpha_input,upper_alpha_input,num_input,special_input=0,0,0,0

user_password = "@HelloW0r1d#"
password_length =len(user_password)

if (password_length >= 6 and password_length<=12):
    for value in user_password:

        # counting lowercase alphabets
        if (value.islower()):
            lower_alpha_input += 1

        # counting uppercase alphabets
        if (value.isupper()):
            upper_alpha_input += 1

        # counting numbers
        if (value.isdigit()):
            num_input += 1

        # counting special characters
        if (value == '$' or value == '#' or value == '@'):
            special_input += 1

if (lower_alpha_input > 0 and upper_alpha_input >0 and num_input >0 and special_input > 0
        and (lower_alpha_input + upper_alpha_input + num_input + special_input) == password_length):
    print("Entered Password is Valid")
else:
    print("Entered Password is InValid")
print('\n')

#####################################################################################################################################

'''
4.
Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9]
Hint: Use Loop to iterate through list elements.
'''
print('Answer for Question 4 Begins ')

a = [4,7,3,2,5,9]

for element in a:
    print('Element',element,'has its position at : ',a.index(element))
print('\n')

#####################################################################################################################################

'''
5.
Please write a program which accepts a string from console and print the characters that have even indexes.
Example: If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be: Helloworld

'''
print('Answer for Question 5 Begins ')

user_input=input("Please provide a input : ")
user_input_list=list(user_input)
user_input_length=len(user_input)
eligible_indexes=[element for element in range(0,user_input_length) if element%2==0]
related_elements=[]
for element in eligible_indexes:
    related_elements.append(user_input_list[element])

even_output = ''.join(related_elements)

print('The Elements at Even positions are :',even_output)
print('\n')

#####################################################################################################################################

'''
6.
Please write a program which accepts a string from console and print it in reverse
order.
Example: If the following string is given as input to the program:
rise to vote sir
Then, the output of the program should be:
ris etov ot esir
'''
print('Answer for Question 6 Begins ')

user_input=str(input("Please enter a sentence : "))
input_list=list(user_input)

input_list.reverse()

listToStr = ' '.join(map(str, input_list))

print('Output is : ',listToStr)
print('\n')

#####################################################################################################################################

'''
7.
Please write a program which count and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
'''

print('Answer for Question 7 Begins ')

my_user_input=str(input("Please enter a word :"))

user_input_set=set(my_user_input)
user_input_list=list(user_input_set)
user_input_list.sort()

for element in user_input_list:
    print(element,',',my_user_input.count(element))
print('\n')

#####################################################################################################################################

'''
8.
With   two   given   lists   [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a
program to make a list whose elements are intersection of the above given lists
'''
print('Answer for Question 8 Begins ')

first_list=[1,3,6,78,35,55]
second_list=[12,24,35,24,88,120,155]

print('Common elements in both the lists are : ',list(set(first_list) & set(second_list)))
print('\n')

#####################################################################################################################################

'''
9.
With a
given list [12,24,35,24,88,120,155,88,120,155], write a program to print this
list after removing all duplicate values with original order reserved.
'''
print('Answer for Question 9 Begins ')

input_list=[12,24,35,24,88,120,155,88,120,155]
unique_list = list(dict.fromkeys(input_list))

print('Unique element list with original order reserved is: ',unique_list)

print('\n')

#####################################################################################################################################

'''
10.
By using list comprehension, please write a program to print the list after removing
the value 24 in [12,24,35,24,88,120,155].
'''
print('Answer for Question 10 Begins ')

user_list=[12,24,35,24,88,120,155]

updated_list = [ x for x in user_list if x != 24]
print('Updated list is :',updated_list)

print('\n')

#####################################################################################################################################

'''
11.
By using list comprehension, please write a program to print the list after removing
the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
'''
print('Answer for Question 11 Begins ')

user_input= [12,24,35,70,88,120,155]

zeroth_element=user_input[0]
fourth_element=user_input[4]
fifth_element=user_input[5]

final_output=[i for i in user_input if (i !=zeroth_element and i!=fourth_element and i!=fifth_element)]

print('Output after removing 0th,4th,5th numbers are',final_output)

print('\n')

#####################################################################################################################################

'''
12.
By using list comprehension, please write a program to print the list after removing
delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
'''
print('Answer for Question 12 Begins ')

user_input= [12,24,35,70,88,120,155]

zeroth_element=user_input[0]
fourth_element=user_input[4]
fifth_element=user_input[5]

final_output=[i for i in user_input if (i%5!=0 or i%7!=0)]

print('Output after removing elements from list which are divisible by 5 and 7 :',final_output)

print('\n')

#####################################################################################################################################

'''
13.
Please  write  a  program  to  randomly  generate  a  list  with  5  numbers,  which  are
divisible by 5 and 7 , between 1 and 1000 inclusive.
'''
print('Answer for Question 13 Begins ')

import random

list_5_7_combination= []
for i in range(0,1001):
    if i%5==0 and i%7==0:
        list_5_7_combination.append(i)

my_set=set(list_5_7_combination)

print('Final Output is :',list(random.sample(my_set, 5)))
print('\n')

#####################################################################################################################################


'''
14.
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
Example: If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
'''

print('Answer for Question 14 Begins ')


input_counter=int(input("Enter a number : "))
n=0
final_sum=0
while n<=input_counter:
    final_sum=final_sum+((n)/(n+1))
    n+=1

print(final_sum)
print('\n')
#####################################################################################################################################
