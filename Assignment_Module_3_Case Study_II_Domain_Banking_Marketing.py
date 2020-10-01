'''

Module 3–Deep Dive -Functions, OOPs, Modules, Errors and Exceptions

Case Study

Domain –Banking Marketing

focus –Optimization

Business challenge/requirement
Bank of Portugal runs marketing campaign to offer loans to clients.  Loan is offered to only clients with particular professions. 
List of successful campaigns(with client data) is given in attached dataset. 
You have to come up with program which reads the file and builds a set of unique profession list and given input profession of client 
–system tells whether client is eligible to be approached for marketing campaign.

Key issues :
Tele Caller can only make x number of cold calls in a day. Hence to increase her effectiveness only eligible customers should be called

Considerations 
Current system does not differentiate clients based on age and profession

Data volume :-
447 records in bank-data.csv

Additional information :- NA

Business benefits :-
Company can achieve between 15% to 20% higher conversion by targeting right clients

Approach to Solve
You have to use fundamentals of Python taught in module 3
1. Read file bank - data.csv
2. Build a set of unique jobs
3. Read the input from command line – profession
4. Check if profession is in list
5. Print whether client is eligible

Refer to CheckForProfessionEligibility.py for solution and bank-data.csv for data Enhancements for code 
You can try these enhancements in code
1. Compute max and min age for loan eligibility based on data in csv file
2. Store max and min age in dictionary
3. Make the profession check case insensitive 
4. Currently program ends after the check. Take the input in while loop and end only if user types "END" for profession

'''

import csv
unique_job=[]

with open('bank-data.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 for row in data:
   unique_job.append((row['job'],int(row['age'])))

unique_job=list(set(unique_job))

def min_age_func(list_unique_job,v_user_profession):
    min_age=[]
    for i in list_unique_job:
        if i[0] == v_user_profession:
            min_age.append(i[1])
        else:
            pass
    return min(min_age)

def max_age_func(unique_job,user_profession):
    max_age = []
    for i in unique_job:
        if i[0] == user_profession:
            max_age.append(i[1])
        else:
            pass
    return max(max_age)

try:
    while True:
        job_yes_counter = 0
        user_profession = str(input('Enter your profession :')).lower()
        for element in unique_job:
            if user_profession == element[0]:
                job_yes_counter += 1
            else:
                pass

        if job_yes_counter >= 1:
            my_user_age = 0
            my_user_age = int(input('Enter your age :'))
            min_age = min_age_func(unique_job, user_profession)
            max_age = max_age_func(unique_job, user_profession)
            if my_user_age >= min_age and my_user_age <= max_age:
                print('Yes, you are eligible for a loan from Bank of Portugal')
            elif my_user_age<min_age:
                print('Sorry, you are not eligible for the loan as your age is too less')
            else:
                print('Sorry, you are not eligible for the loan as your age is too high')
        else:
            print('Sorry, you are not eligible for the loan.')

        user_acceptance = str(
            input('Do you wish to continue ? : \n 1. Press Y for Yes \n 2. Press N for no \n')).lower()
        if user_acceptance == 'y' or user_acceptance == 'yes':
            continue
        else:
            break
except:
    print('Wrong input entered')
finally:
    print('Thank you !')