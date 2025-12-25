# Data Structures
# • Arrays, lists, tuples and sets
# • Stacks and queues
# • Dictionaries
# • Comprehensions
# • Generator expressions 

# 1. Difference between Arrays, lists, tuples and sets
# Pythondagi list lar tartibli va har xil typega ega o'zgaruvchi ma'lumotlarni o'z ichida saqlaydi. O'zining soddaligi va moslashuvchanligi sababli Pythonda ishlatiladigan data structerlardan

# Key Characteristics:
# Mutable: Elements can be modified after creation.
# Ordered: Maintains the order of elements.
# Allows Duplicates: Can have multiple occurrences of the same value.
# Heterogeneous: Can store different data types.

# creating a list
# a = [1,2,'Python', True, '$', 1.5]

# # accesing elements by indexing
# print(a[0])
# print(a[-1])

# # Modifiying an element
# a[1] = 'Updated'
# # print(a[1])
# print(a)

# # Appending an element
# a.append('Last element')
# print(a)

# # Removing an element
# a.remove(1.5)
# print(a)

# # List slicing 
# print(a[1:5])



# Set in Python
# Set bu python dagi tartiblanmagan va unique yani qaytarilmaydigan elementlardan tashkil topgan kolleksiya. Ko'pincha qaytariladigan elementlardan halos bo'lish uchun foydalaniladi.

# Key Characteristics:

# Mutable: Elements can be added or removed.
# Unordered: Does not maintain the order of elements.
# Unique Elements: Duplicate values are automatically removed.
# Heterogeneous: Can store different data types.

# creating set 
# s = {1,1,2,3,3,True,True,False,'Python', 'Java', 'Js', 'Java'}
# print(s)

# # adding an element
# s.add(5)
# print(s)

# # removing an element
# s.remove(3) # KeyError if the element is not present
# print(s)

# Accessing elements (No indexing because it is unordered)
# print(s[0])
# s[0] = True

# for el in s:
#     print(el)

# Tuple in Python
# Python dagi tartiblangan lekin o'zgartirib bo'lmaydigan elementlar kolleksiyasi (to'plami). Ularni asosan element yaratilgandan keyin o'zgartirilmasligi uchun foydalaniladi.

# Key Characteristics:
# Immutable: Once created, elements cannot be modified.
# Ordered: Maintains the order of elements.
# Allows Duplicates: Can contain duplicate values.
# Heterogeneous: Can store different data types.

# # creating tuple
# tup = (1,2,3,'Python', 2)
# print(tup)

# # accesing elements by indexing
# print(tup[0])
# print(tup[-1])

# # tuple slicing
# print(tup[1:4])

# # Attemping to modify a tuple (Raises TypeError)
# # tup[1] = 'new_value' # Uncommenting this will raise an error



# Practice simple login 

# users = []

# def login():
#     while True:
#         username = input('Enter your name (or type `exit` to stop): ').strip()

#         if username == '':
#             print('Name cannot be empty')
#             continue

#         elif username.lower() == 'exit':
#             break
#         else:
#             users.append(username)
#             print(f'Current users lists: {users}')
    
#     return users


# def remove():
#     while True:
#         if not users:
#             print('users list is empty')
#             break
        
#         print('Current users lists: ', users)
#         name = input('Enter name (or type `exit` to stop): ').strip()

#         if name.lower() == 'exit':
#             break
#         elif name in users:
#             users.remove(name)
#             print(f'User {name} removed, users lists: {users}')
#         else:
#             print('User not found!')
    
#     return users

# l = login()
# r = remove()
# print('Final users lists: ', users)

# users = []
# def add_name():
#     while True:
#         name = input('Enter name (or `exit` command for stop): ').strip()

#         if not name:
#             print('name cannot be empty')
#             continue 

#         elif name.lower() == 'exit':
#             print('The app stopped!')
#             break

#         else:
#             users.append(name)
#             print(f'User list: {users}')
#     return users

# add_name()

# 2 task
# l = ['John', 'Darek', 'John', 'Ronald', 'Darek']

# l_into_s = set(l)

# print(l_into_s)

# # 3 task
# tup = (16, 'February', 2005)
# print(tup[1])


# Stacks and Queues
#  Stacks va Queues — bu data structure lar bo‘lib, real hayotdagi tartib va navbat mantiqini kodda ifodalaydi. Juda ko‘p joyda ishlatiladi: backend, OS, browser, undo/redo, task scheduling va hokazo.

# STACK - LIFO - Last In, First Out - oxirgi kirgan - birinchi chiqadi

# 🍽 Real hayot misoli

# Idishlarni ustma-ust qo‘yish:

# Oxirgi qo‘yilgan likopcha

# birinchi olinadi

# stack = []

# stack.append('a')
# stack.append('b')
# stack.append('c')

# print(stack)

# el = stack.pop()

# print(el)
# print(stack)


# QUEUE (Navbat)
# FIFO - First In, First Out
# Birinchi kirgan — birinchi chiqadi.

# 🎟 Real hayot misoli

# Do‘kondagi navbat:

# Birinchi kelgan odam

# birinchi xizmat oladi

# queue = []

# queue.append('a')
# queue.append('b')
# queue.append('c')

# print(queue) 
# el = queue.pop(0)
# print(el)
# print(queue)


# from collections import deque 

# queue = deque()

# queue.append('User1')
# queue.append('User2')
# queue.append('User3')

# print(queue)

# queue.popleft()
# queue.appendleft('5')
# print(queue)

