#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1. Explain with an example each when to use a for loop and a while loop.


# In[ ]:


The for loop is used when we know the number of iterations, that is, how many times a statement must be executed.
That is why, when we initialize the for loop, we must define the ending point. 
for example: l=[1,2,3,4,5]
 for i in l:
        print(i)
1
2
3
4
5

A while loop is used when the number of iterations is unknown. It is used when we need to end the loop on a condition other than
the number of repetitions.It is not necessary to know the condition ahead of time in this case. That is why we can use a boolean
expression in the loop's initialization.
for example: 


# In[9]:


#Q2. Write a python program to print the sum and product of the first 10 natural numbers using for and while loop.


# In[12]:


#sum of first 10 number using while loop 
n = int(input("enter your limit"))
starting_point = 0
counter = 1

while counter <= n:
    starting_point = starting_point + counter
    counter = counter +1
starting_point


# In[13]:


#sum of first 10 number using for loop
num = int(input("Please enter the number: "))

sum = 0

for value in range(1, num + 1):
    sum = sum + value
    
print(sum)


# In[14]:


#product of first 10 number using while loop
n = int(input("enter your limit"))
starting_point = 1
counter = 1

while counter <= n:
    starting_point = starting_point * counter
    counter = counter +1
starting_point


# In[15]:


#product of first 10 number using for loop
num = int(input("Please enter the number: "))

product = 1

for value in range(1, num + 1):
    product = product* value
    
print(product)


# In[ ]:


#Q3. Create a python program to compute the electricity bill for a household.The per-unit charges in rupees are as follows: 
#For the first 100 units, the user will be charged Rs. 4.5 per
#unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
#be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
#You are required to take the units of electricity consumed in a month from the user as input.
#Your program must pass this test case: when the unit of electricity consumed by the user in a month is
#310, the total electricity bill should be 2250.


# In[18]:


unit= int(input("enter your unit"))
if unit<=100:
    bill=unit*4.5
elif unit>= 101 and unit <=200:
    bill= 450+((unit-100)*6)
elif unit>=201 and unit<=300:
    bill= 450+600+((unit-200)*10)
else:
    bill=450+600+1000+((unit-300)*20)


# In[19]:


bill


# In[ ]:


#Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
#number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print that list.


# In[8]:


l = list(input("Please enter the number: "))
output=[0,100,1]
for i in l:
    if (l**3)%4==0 or (l**3)%5==0:
        output.append(l)        print(output)


# In[ ]:


#Q5. Write a program to filter count vowels in the below-given string.
#string = "I want to become a data scientist"


# In[20]:


string = input('String: ')
vowels = [each for each in string if each in "aeiouAEIOU"]
print('Number of vowels in string:', len(vowels))
print(vowels)


# In[ ]:




