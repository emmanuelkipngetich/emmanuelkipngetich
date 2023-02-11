#!/usr/bin/env python
# coding: utf-8

# # SIMPLE CALCULATOR PROJECT
# 
# 

# In[ ]:


#Ask for two numbers 
#Apply an operation

print("My python calculator!")

first_number = float(input("Please enter your first number"))
second_number = float(input("Please enter your second number"))

print("Enter 'a' for addition")
print("Enter 'b' for subtraction")
print("Enter 'c' for multiplication")
print("Enter 'd' for division")
print("Enter 'q' to quit")

operation = input("Please enter operation: ").lower()

if operation == "a":
    answer = first_number + second_number
    print(answer)
elif operation == "b":
    answer = first_number - second_number
    print(answer)
elif operation == "c":
    answer =  first_number * second_number
    print(answer)
elif operation == "d":
    if second_number != 0:
        answer = first_number / second_number
        print(answer)
    else:
        print("Can't divide by 0")
else:
    answer = "Quit"
    print(answer)


