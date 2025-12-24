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

