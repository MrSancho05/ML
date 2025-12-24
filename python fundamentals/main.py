# FOR BEGINNERS
# 1. simple calculation
# num1 = int(input('1chi sonni kiriting: '))
# num2 = int(input('2chi sonni kiriting: '))
# action = input('Ikkta son ustida bajarmoqchi bo`lgan amalni kiriting: ')

# def calcutation(n, n2, ac):
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
#             return f'{n} % {n2} = {n % n2}'
    
    
# c = calcutation(num1, num2, action)

# print(c)


# 2. Even or Odd
# print('\n')
# print('2nd Task')
# num = int(input('Son kiriting: '))

# def even_or_odd(n):
#     if n <= 0:
#         return 'The number must be greater then 0'
    
#     if n % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'


# result = even_or_odd(num)
# print(result)


# 3. from 1 to N
# n = int(input('Enter n number: '))

# for i in range(1, n):
#     print(i)


# INTERMIDIATE
# 1. Grade system
# print('Grade system')
# score = int(input('Enter your score, to get result: '))

# def grade(s):
#     if 90 <= s <= 100:
#         return 'A'
#     elif 75 <= s <= 89:
#         return 'B'
#     elif 60 <= s <= 74:
#         return 'C'
#     else:
#         return 'F'
    
# result = grade(score)
# print(f'Your grade is {result}')

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


# print(f'Max number is: {max_number}') 
# print(f'Min number is: {min_number}') 
# print(f'Medium arifmetics: {medium_arifmetic // 5}')


# 3. Check password
print('Check password')
correct_password = 'hiBye'
password = input('Enter password: ')

while True:
    if correct_password == password:
        print('Welcome!')
        break
    else:
        print('Wrong password!')
        password = input('Enter password: ')

    

