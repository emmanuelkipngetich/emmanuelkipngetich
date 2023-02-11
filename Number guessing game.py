#!/usr/bin/env python
# coding: utf-8

# # Number guessing game

# In[1]:


#program generates a random number between 1 and 15
#Allows the player to submit a guess for a random number between 1 and 15
#Checks the users guess against actual answer.output "wrong guess try again", depending on the user's incorrect answer.
#if they get the answer correct, show the actual answer to the player and the end game


# In[6]:


#Import the random library
import random
#Welcome message 
print("Welcome to the number guessing game")

#Generate a random number 
random1 = random.randint(1, 15)
print(f"random number is: (random1)")
# Allow user to guess
user_guess = int(input("Guess a number between 1 and 15: "))
    
#Compare user guess to random number

if user_guess > random1:
    print("Wrong guess, try again! ")
elif user_guess < random1:
    print("Wrong guess, try again!")
else:
    print(f"You have won. The random number is (random1)")


# In[ ]:




