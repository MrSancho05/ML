# TASKS FOR BEGINNERS
# 1. simple calculation
# print('Simple calculation')
# num1 = int(input('1chi sonni kiriting: '))
# num2 = int(input('2chi sonni kiriting: '))
# action = input('Ikkta son ustida bajarmoqchi bo`lgan amalni kiriting: ')

# def calculation(n, n2, ac):
#     match ac:
#         case '+':
#             return f'{n} + {n2} = {n + n2}'
#         case '-':
#             return f'{n} - {n2} = {n - n2}'
#         case '*':
#             return f'{n} * {n2} = {n * n2}'
#         case '/':
#             if n2 == 0:
#                 return '0 ga bo`lib bo`lmaydi'
#             return f'{n} / {n2} = {n / n2}'
#         case '//':
#             if n2 == 0:
#                 return '0 ga bo`lib bo`lmaydi'
#             return f'{n} // {n2} = {n // n2}'
#         case '%':
#             if n2 == 0:
#                 return '0 ga bo`lib bo`lmaydi' 
#             return f'{n} % {n2} = {n % n2}'
    
    
# c = calculation(num1, num2, action)

# print(c)


# 2. Even or Odd
# print('Even or Odd')
# num = int(input('Son kiriting: '))

# def even_or_odd(n):
#     return 'Even' if n % 2 == 0 else 'Odd'

# result = even_or_odd(num)
# print(result)


# 3. from 1 to N
# n = int(input('Enter n number: '))
# total = 0

# for i in range(1, n):
#     total += i
#     print(i)

# print(f'Sum: {total}')


# TASKS FOR INTERMIDIATE 
# 1. Grade system
# print('Grade system')
# score = int(input('Enter your score, to get result: '))

# def grade(s):
#     if 90 <= s <= 100:
#         return 'Your grade is: A'
#     elif 75 <= s <= 89:
#         return 'Your grade is: B'
#     elif 60 <= s <= 74:
#         return 'Your grade is: C'
#     elif not 0 <= s <= 100:
#         return 'Invalid score'
#     else:
#         return 'Your grade is: F'
    
# result = grade(score)
# print(result)

# 2. Statistics of nums
# print('Statistics of numbers')
# num = int(input('Enter 1st number: '))
# num2 = int(input('Enter 2nd number: '))
# num3 = int(input('Enter 3rd number: '))
# num4 = int(input('Enter 4th number: '))
# num5 = int(input('Enter 5th number: '))

# nums = []
# nums.append(num)    
# nums.append(num2)
# nums.append(num3)
# nums.append(num4)
# nums.append(num5)

# max_number = num
# min_number = num
# medium_arifmetic = 0

# for i in range(len(nums)):
#     if max_number <= nums[i]:
#         max_number = nums[i]
#     if min_number >= nums[i]:
#         min_number = nums[i]
    
#     medium_arifmetic += nums[i]

# print(f'Max number is: {max_number}, with max func {max(nums)}') 
# print(f'Min number is: {min_number}, with min func {min(nums)}') 
# print(f'Medium arifmetics: {medium_arifmetic / len(nums)}')
# print(sum(nums))

# 3. Check password
# print('Check password')
# correct_password = 'hiBye'
# password = input('Enter password: ')
# attemps = 3

# while True:
#     if correct_password == password:
#         print('Welcome!')
#         break
#     else:
#         attemps -= 1
#         if attemps == 0:
#             print('Your attemps is over:(')
#             break
#         print(f'Wrong password! \n You have {attemps} attemps!')
#         password = input('Enter password: ')


# TASKS FOR ADVANCED 
# print('Global 🌍 & Local 🏡')
# 1. SCOPE
# global_var = 10

# def func():
#     local_var = 5
#     global global_var

#     global_var += 1
#     return local_var

# local_var = func()
# print(global_var, local_var)


# 2. COUNT NUMBERS
# print('Number statistic 📈')
# count_nums = 0
# positive_nums = 0
# negative_nums = 0
# zero_count = 0

# while True:
#     n = int(input('Enter number: ')) 

#     if n > 0:
#         positive_nums += 1
#     elif n < 0:
#         negative_nums += 1
#     else:
#         zero_count += 1
#         break
#     count_nums += 1

# print(f'Numbers count: {count_nums}')
# print(f'Positive numbers count: {positive_nums}')
# print(f'Negative numbers count: {negative_nums}')
# print(f'Numbers of zero: {zero_count}')


# 3. Nested function
# num = int(input('Enter 1st number: '))
# num2 = int(input('Enter 2nd number: '))
# action = input('(add/substract/multiply/divide): ')

# def calculator(n,n2):
#     match action:
#         case 'add':
#                 return n + n2
#         case 'substract':
#                 return n - n2
#         case 'multiply':
#                 return n * n2
#         case 'divide':
#                 if n2 == 0:
#                     raise ZeroDivisionError("Cannot divide by zero")
#                 return n // n2
#         case _:
#                 return 'Invalid operation'

# calc = calculator(num, num2)
# print(calc)


# Data types in Python
# Python’da data type — bu ma’lumotning qaysi turga tegishli ekanini bildiradi.
# Ma’lumot turi uning ustida qanday amal bajarish mumkinligini aniqlaydi.
# Numeric: int, float, complex
# Sequence Type: string, list, tuple
# Mapping Type: dict
# Boolean: bool
# Set Type: set, frozenset
# Binary Types: bytes, bytearray, memoryview

# Python’da hamma narsa object hisoblanadi:

# Data type → class

# Variable → shu class’dan olingan object
# Example of numeric types in Python

a = 10
b = 10.5
c = 2 + 4j

print(a, b, c)
print(type(a), type(b), type(c))

# Output 
# <class 'int'> <class 'float'> <class 'complex'>

# Example None and bool types
# a = True
# b = None

# print(type(a), type(b))


# Sequence - ketma-ket ma'lumotlarni o'zida saqlaydigan

# s = 'Welcome to the Sequence world'

# print(s, type(s))

# print(s[8:])
# print(s[2])
# print(s[3])


# type() build-in function
# numeric
n = 10
n2 = 10.2

print(type(n), type(n2))


# sequence list, str, set, tuple

l = [1,2,3] # integer list
l2 = ['apple', 'orange', 'mango'] # string list
l3 = [1, 1.5, 'lemon', True, [1,2,3]] # mixed list

print(l3[0:3])

l3[0] = 'text'
l3[2] = 'orange'

print(l3)

l3.remove(True)

print(l3)

l3.pop()

print(l3)

# set
s = {'first', 1, 2}



