# Introduction to Python

#####################################################################################################################################

'''
1.
Write a program which will find factors of given number and find whether the
factor is even or odd. Hint: Use Loop with if-else statements
'''

print('Answer for Question 1 Begins ')

class UnAcceptedValueError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

while True:
    try:
        input_number = int(input("Enter a natural number : "))
        if input_number<=0:
            raise UnAcceptedValueError("Sorry entered number cannot be less than 1 ! Please try again ...")
        break
    except UnAcceptedValueError as e:
        print("Received error:", e.data)
    except ValueError:
        print("No valid natural number entered ! Please try again ...")
        print("Hint : Natural number starts with 1 !!!")

counter=1
factors_of_input=[]
while input_number>=counter:
    if input_number%counter==0:
        factors_of_input.append(counter)
        counter += 1
    else:
        counter += 1
        continue

len_of_factors=len(factors_of_input)

if len_of_factors%2==0:
    even_or_odd='Even'
else:
    even_or_odd='Odd'

print('Factors of input number',input_number,'are :',factors_of_input,'& the factor is',even_or_odd)
print('\n')

#####################################################################################################################################

'''
2.
Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
Hint: In case of input data being supplied to the question, it should be assumed to be a console input
'''
print('Answer for Question 2 Begins ')

input_word=str(input("Enter a word : "))
intermediate_word=(input_word.split(sep=" "))
old_word=intermediate_word
intermediate_word.sort(key=lambda y: y.lower())
sorted_word=' '.join(map(str, intermediate_word))
print('Word before sorting : ',input_word)
print('Word after sorting  : ',sorted_word)
print('\n')

#####################################################################################################################################

'''
3.
Write a program, which will find all the numbers between 1000 and 3000 (both included) such that each digit of a number
is an even number. The numbers obtained should be printed in a comma separated sequence on a single line.
Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
Divide each digit with 2 and verify is it even or no
'''

print('Answer for Question 3 Begins ')

for i in range(1000,3001):
    split_numbers = [int(j) for j in str(i)]
    if ((split_numbers[0] % 2 == 0) and (split_numbers[1] % 2 == 0) and (split_numbers[2] % 2 == 0) and (split_numbers[3] % 2 == 0)):
        listToStr = ''.join(map(str, split_numbers))
        print(listToStr, end=",")
    else:
        pass

print('\n')

######################################################################################################################################

'''
4.
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose if the entered string is: Python0325 Then the output will be:
LETTERS: 6
DIGITS:4
Hint: Use built -in functions of string.
'''
print('Answer for Question 4 Begins ')

text_input=input('Enter a Letter: ')

numeric_count=0
alphabet_count=0

for letter in text_input:
    if letter.isnumeric()==True:
        numeric_count+=1
    elif letter.isalpha()==True:
        alphabet_count+=1
    else:
        pass
print('LETTERS: ',alphabet_count)
print('DIGITS: ',numeric_count)
print('\n')
######################################################################################################################################

'''
5.
Design a code which will find the given number is Palindrome number or not.
Hint: Use built -in functions of string.
'''
print('Answer for Question 5 Begins ')

while True:
    try:
        user_input = int(input("Please Enter a non negative number : "))
        user_input_string = str(user_input)
        my_list = []
        for number in user_input_string:
            my_list.append(number)

        reversed_user_input = list(reversed(my_list))

        combined_reversed_string = ''.join(reversed_user_input)
        combined_reversed_number = int(combined_reversed_string)

        if user_input == combined_reversed_number:
            print('The given number is a Palindrome ')
        else:
            print('The given number is not a Palindrome')
        break
    except ValueError:
        print("Exception : Negative or Alphanumeric entered \n")
print('\n')
######################################################################################################################################
