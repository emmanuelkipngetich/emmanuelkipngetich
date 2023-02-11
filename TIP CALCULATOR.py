#!/usr/bin/env python
# coding: utf-8

# In[13]:


# ask the user to enter the charge for the food.
print("""Hello there. Welcome to Asanka Hotel. 

We serve the best! """)

print("............................................")

Charge_for_food = float(input("Enter the price of the food ordered: $"))

#calculate the amounts of an 18 percent tip and 7 percent sales tax on the charge of the food and display each of these amounts

if Charge_for_food > 0:
    tip_charged = 0.18*Charge_for_food
    print("Tip = + (tip_charged)")
    sales_tax_charged = 0.07*Charge_for_food
    print(sales_tax_charged)
    Total_charge = tip_charged + sales_tax_charged + Charge_for_food
    print(Total_charge)
else:
    print("Wrong entry. Try again")
    


# In[ ]:




