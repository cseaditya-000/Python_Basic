# name="Beau" #indentation  matters in python
# print(type(name)==str) #This is used to know the data type of variable. And also we could directky compare the data type to probable using ==.
# print(isinstance(name,str)) #This checks whether object belongs to a specific class or data type
# Float, int, str,
# age=int("20")
# print(age)
# complex for complex numbers
# bool for booleans
# list for lists
# tuple for tuples
# range for ranges
# dict for dictionaries
# set for sets
# ********Operator**********
# = is assignment operator.
# +(addition),-(subtraction),*(multiplication),/(division),%(modulus),**(square),//(floor division) are mathematical operators
# age=83#This operator could be used with any mathematical operator. They means similar. This used to shorten the code.
# age+=9#this means age=age +9
# print(age)
# ==,!=,>,<,<=,>= are comparison operators.
# == check whether equal to
# !- checks whether not equal to. Others are obvious.
# Boolean operator True or False
## OR Operator ## Checks first if first is true then returns the first and if it is fslse then it returns the second as output
# print(0 or 1) #1 //0--fakse and 1--False
# print(False or 'hey') #hey
# print('hi' or 'hey') #hi
# print([] or False) #False as [] is considerded a false value
# print(False or []) # [] as Flase is also a false value
# # AND Operator ## Evaluates whether first is true or false. if first is true then it moves on to second and if first is false then it gives the first value as output wihthout checking the second 
# print(0 and 1) #0
# print(1 and 0) #0
# print(False and 'hey') #False
# print('hi' and 'hey') #hey
# print([] and False) #[]
# print(False and []) #False
## BITWISE OPERATOR ##
# is--Identity Operator
# in--Memebership Operator
#       Ternary Operator        # 
# def is_adult(age):
#     if age > 18:
#         return True   #without ternary operator
#     else:
#         return False
    
# def is_adult2(age):           #with teernary operator
#     return True if age>18 else False #Everything on a single line

#Strings in python 
# "Adi"
# 'Adi'
# name='Adi'
# phrase=name+' is my name'
# name+=' is my name'
# print(name)
# age=str(38)
# print("""Adi is

# 19
      
#       years old
# """)#multi line string
# print("adi".upper())#Changes to upper case all
# print("ADi".lower())#changes to lower case all
# print("adi doIng things".title())#Changes the first letter of each word to capital and remaing to small
# print("adea".islower())#used to check whether it is all lower letters
a=str(123)
print(a+"j")