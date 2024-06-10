#!/usr/bin/env python
# coding: utf-8

# # # Question 1

# In[14]:


import math as m
# 1st part
S = 7*(m.log(3))*(m.log(5) + m.log(m.exp(3)))
print('The value of the expression is =',S)

# 2nd part
d1 = 5 # diameter of the 1st circle
d2 = 3 # diameter of the 2nd circle

A1 = m.pi*(d1/2)**2 # Area of the 1st circle
A2 = m.pi*(d2/2)**2 # Area of the 2nd circle
d = A1 - A2
print('The difference of the areas of the circles is = ', d)


# In[4]:


help(m)


# # Question 2

# In[12]:


OddNum = (80 // 2) - (7 // 2)
EvenNum = (80 // 2) - (7 // 2)
#print('Number of odd numbers',OddNum)
#print('Number of even numbers',EvenNum)

print("Number of odd numbers: {}, Number of even numbers: {}".format(OddNum, EvenNum))


# # Question 3

# In[44]:


import sys
# different variables
integer_var = 42
float_var = 3.14
string_var = "Hello"
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
set_var = {7, 8, 9}
dict_var = {'a': 10, 'b': 11, 'c': 12}
bool_var = True

# Create a list of variables for 
variables = [integer_var, float_var, string_var, list_var, tuple_var, set_var, dict_var, bool_var]

# Function to print information about each variable
def print_variable_info(var):
    size = sys.getsizeof(var)
    data_type = type(var).__name__
    print(f"{data_type}: {var}, Size: {size} bytes")

# Print information about each variable
for var in variables:
    print_variable_info(var)
    
def var_Size(var):
    size = sys.getsizeof(var)
    return size
    
size_list = [var_Size(integer_var),var_Size(float_var),var_Size(string_var),var_Size(list_var),var_Size(tuple_var),var_Size(set_var),var_Size(dict_var),var_Size(bool_var)]
sorted_size_list = sorted(size_list)
print("The size list of the variables in acending order",sorted_size_list)


# # Question 4

# In[18]:


import random as rd
seedValue = int(input('Enter the seed value:'))
rd.seed(seedValue)
# we are generating random integers between 10 and 100
a = rd.randint(10,100)
b = rd.randint(10,100)
c = rd.randint(10,100)

# Calculating Surface area
S = 2*(a*b + b*c + c*a)
print("The sides of the cuboid are a = {}, b = {}, c = {}".format(a,b,c))
print('The surface area is = ',S)


# # Question 5

# In[14]:


# We are finding roots of a quadratic equation ax^2+bx+c=0
import math as m
p = int(input("Enter the coeffitient of x^2, a (a!=0): "))
if p==0:
    print("In quadratic equation coeffitient of x^2 should be non zero, Enter again the value of a ")
    
else:
    a = p
    b = int(input("Enter the coeffitient of x, b: "))
    c = int(input("Enter the  constant, c: "))
d = (b*b - 4*a*c) # d = Discriminent

if d>=0:
    print("The roots are real:")
    r1 = (-b +m.sqrt(d))/(2*a)
    r2 = (-b - m.sqrt(d))/(2*a)
    print("Roots are r1 = {}, r2 = {}".format(r1,r2))
else:
    print("The roots are complex")


# 
# #  Question 6

# In[22]:


a,b = input("Enter two integers:").split()
a = int(a)
b = int(b)
# Addition
print("The addition of two integers is: ",a+b)
# Subtruction
print("The subtruction of two integers is: ",a-b)
# Multiplication
print("The multiplication of two integers is: ",a*b)
# Division
if b==0:
    print("For division denominator should be non zero")
else:
    print("The division of two integers is: ",a/b)

# Remainder
if b==0:
    print("For division denominator should be non zero")
else:
    print("The remainder is: ",a%b)

# Exponent
print("The exponent (a^b) is: ",a**b)



# # Question 7

# In[29]:


# Given words
words = ['Learning', 'python', 'is', 'fun']

#  Create a sentence by combining these words using '.join'
s1 = " ".join(words)
print("The sentence is: ", s1)

# Print the sentence "Learning datascience is fun." using '.replace'
s2 = words.replace('python', 'datascience')
print(" Modified sentence:", s2)

# Generate an uppercase version of the sentence: "LEARNING PYTHON IS FUN."
s3 = words.upper()
print(" Uppercase sentence:", s3)

#  Rearrange the words to form a new sentence: "fun is python learning."
s4 = ' '.join(words[::-1])
print("Rearranged sentence:",s4)



# # Question 8

# # Python allocates memory dynamically and other languages are works statically.

# In[ ]:





# # Question 9

# # The built-in function in python are those functions which comes with python, which we can use without importing the libraries.

# # 1) abs() which returns the absolute value of a number
# # 2) float() which returns a floating point number
# # 3) help()  which executes the built-in help system
# # 4) len()    which returns the length of an object
# # 5) print() Prints to the standard output device

# # Question 10

# In[39]:


# function for counting vowels in a string
def count_vowels(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for letter in string:
        if letter in vowels:
            vowel_count += 1

    return vowel_count

Str = input("Enter a string: ")
n = count_vowels(Str)
print("The number of vowels in the given string is:",n)


# In[ ]:


# Checking if a given string is palindrome or not
str1 = input("Enter a string: ")
rev_str = str1[::-1]

if str1.lower() == rev_str.lower():
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

