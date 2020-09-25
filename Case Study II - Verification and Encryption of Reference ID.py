'''
Case Study Domain – Telecom
            Focus – Optimization

Business challenge/requirement :-
LifeTel  Telecom is the latest entrant in the highly competitive Telecom market of Singapore.
It issues SIM to the verified users.  Till now verification was manual through the photocopy of approved id card document.
However government has recently introduced Social ID called Reference ID which is mapped to fingerprint of user.
LifeTel should now verify user against the fingerprint and Reference ID

Key issues :-
Build a system where when user enters Reference ID it is encrypted, so that hackers cannot view the mapping of Reference ID
and finger print.

Considerations :-
System should be secure

Data volume :-
NA

Additional information :-
NA

Business benefits :-
Company will be able to quickly issue SIM to user and expected gain in volume is approximately 10 times as the manual
process of verification is replaced with secure automated system

Approach to Solve :-
You have to use fundamentals of Python taught in module 2
1. Read the input from command line – Reference ID
2. Check for validity – it should be 12 digits and allows on number and alphabet
3. Encrypt the Reference ID and print it for reference

Enhancements for code :-
You can try these enhancements in code
1. Allow some special characters in ReferenceID
2. Give the option for decryption to user
'''

customer_input = str(input("Enter a Reference ID : "))
customer_input_utf = customer_input.encode()
input_length =len(customer_input)

lower_alpha_input,upper_alpha_input,num_input,special_input=0,0,0,0

if (input_length==12):
    for value in customer_input:

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
        if (value.isalnum()==False):
            special_input += 1

if (lower_alpha_input > 0 and upper_alpha_input >0 and num_input >0 and special_input > 0
        and (lower_alpha_input + upper_alpha_input + num_input + special_input) == input_length):
    print("Entered Reference ID is Valid")
    print("The encrypted Reference ID is :",customer_input_utf)
else:
    print("Entered Reference ID is InValid")
