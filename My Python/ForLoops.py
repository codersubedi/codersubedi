#  For Loop

# nums = [1, 2, 3, 4, 5]

# for val in nums:
#     print(val)

# veggies = ["Potato", "brijal", "ladyfinger", "cucumber"]

# for val in veggies:
#     print(val)

# tup = (1, 2, 3, 4, 2, 8, 9)

# for val in tup:
#     print(val)

# names = ("Sandip", "Subedi", "Harry", "Roman", "Heroics")

# for name in names:
#     print(name)

# str = "SandipSubedi"

# for char in str:
#     print(char)
# else:
#     print("END")    

# name = "SubediSandip"

# for char in name:
#     if(char == "d"):
#         print("d found")
#         break    
#     print(char)



# print("Program end")

# name = "Mindrisers"

# for val in name:
#     if (val == "d"):
#         print("d found")
#         break
#     print(val)
# print("END")    


# Print the elements of the following list using a loop
# [1, 4, 9, 16, 25, 36, 49, 72, 81, 100]

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for el in nums:
#     print(el)

# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 49

# idx = 0

# for el in nums:
#     if (el == x):
#         print("Found at idx",idx)
#     idx += 1

# names = ("Ramesh", "Suresh", "Jashwant", "Sunderlal", "Champaklal", "Bhagat-Singh", "Jethalal", "iyer-bhai", "MethaShab")

# Z = "Jethalal"

# idx = 0

# for el in names:
#     if (el == Z):
#         print("Found at idx", idx)
#     idx += 1    

# Range 

# Range functions returns a sequence of numbers,  startinf from 0 by default, and increments by 1(by default), and stops before a specified number

# range( start?, stop, step?)

# for el in range(5):
#     print(el)

# for el in range(1, 5):
#     print(el)

# for el in range(1, 5, 2):
#     print(el)

# for i in range(10):    # range(stop)
#     print(i)

# for i in range(2, 10):   # range(start, stop)
#     print(i)

# for i in range(2, 10, 2):    # range(start, stop, step)
#     print(i)

# for i in range(2, 100, 2): # range(start, stop,step)
#     print(i)

# for i in range(1, 100, 2):
#     print(i)

# Print numbers from 1 to 100

# for i in range(1, 100):
#     print(i)

# Print numbers from 100 to 1

# for i in range(101, -1, 1):
#     print(i)

# for i in range(101, 0, -1):
#     print(i)

# Print the multiplication of a number n.

# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(num*i)

# Pass Statements

# Pass is a null statement that does nothing. It is used as a placeholder for future code

# for el in range(10):
# pass

# for i in range(10):
#     pass

# print("Some useful work")

# WAP to find the sum of first n numbers. (using while loop)

num = int(input("Enter a number: "))

sum = 0
for i in range(1, num+1):
    sum += i
print("Total sum = ", sum)    