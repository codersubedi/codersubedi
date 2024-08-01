# Loops in Python

# Loops are used to repeat instructions

# While loops

# while condition :
# some work

# count = 1
# while count <= 5:
#     print("Hello")
#     count += 1

# i = 1
# while i <= 10:
#     print("Sandip_Subedi")
#     i += 1    

# i = 1 means where to start
# i <= 10 means where to stop
# i += 1 means the space or gap to run the loop    

# Print numbers from 1 to 5

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# print("Loop Ended")

# Print numbers from 5 to 1

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# Print numbers from 1 to 100

# num = 1
# while num <= 100:
#     print(num)
#     num += 1

# Print numbers from 100 to 1

# num = 100
# while num >= 1:
#     print(num)
#     num -= 1

# Print the multiplication table of a number n

# n = int(input("Enter a number you want to multiply: "))

# num = 1
# while num <= 10:
#     print( n * num)
#     num += 1

# Print the multiplication table of 7

# num = 7

# i = 1
# while i <= 10:
#     print(num * i)
#     i += 1

# Write a python program to multiply two numbers provided by the user

# num1 = int(input("Enter a number: "))

# i = 1
# while i <= 10:
#     print(num1 * i)
#     i += 1

# num2 = int(input("Enter another number: "))

# i = 1
# while i <= 10:
#     print(num2 * i)
#     i += 1

# Create a function "multiply_list" that takes a list of numbers and returns the product of all the numbers in the list

# def multiply_list():
#     num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     i = 1
#     while i <= 10:
#         print(num[0] * i)
#         print(num[1]* i)
#         i += 1
# multiply_list()     

# Write a python program to multiply a number by 2, 5 and 10 and display the results

# num = int(input("Enter a number: "))

# i = 2
# while i <= 10:
#     print(num * i)
#     i += 1

# num1 = int(input("Enter another number: ")) 

# i = 5
# while i <= 10:
#     print(num1 * i)
#     i += 1

# num2 = int(input("Enter a number: "))

# i = 10
# while i == 10:
#     print(num * i)
#     i += 1

# Print the element of the following list using a loop
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# idx = 0
# while idx <= len(nums)-1:
#     print(nums[idx])
#     idx += 1


# schools = ["Srijana", "Shivalaya", "Xaviour", "CCRC", "Kantipur", "KMC", "Sunway", "Herald", "Motherland", "Amarsingh"]

# idx = 0

# while idx < len(schools):
#     print(schools[idx])
#     idx += 1


# Search for a number x in this tuple using loop
# (1, 4, 9, 16, 25, 36, 49, 64, 72, 81, 100)

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 72, 81, 100)

# x = 36

# idx = 0
# while idx < len(nums):
#     if (nums[idx]== x):
#         print("FOUND at idx", idx)
#     else:
#         print("Founding...")
#     idx += 1        

# i = 1

# while i <= 5:
#     print(i)
#     if (i == 3):
#         break
#     i += 1
# print("End of loop") 

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) 

x = 36

idx = 0
while idx < len(nums):
    if (nums[idx] == x):
        print("Found at idx", idx)
        break
    else:
        print("Finding..")

    idx += 1    
print("End of loop")    