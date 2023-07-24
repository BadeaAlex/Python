import random

print("<<= Welcome! I'm Nicolae Alexandru Badea and this is Task 1 of the assignment =>>")
print("This program generates a list of 100 random numbers and then it will remove the duplicates")
print("Before every step, you will be asked to press Enter to continue")

print() # Print an empty line to make the output more readable

# Generate a list of 100 random numbers
input("Press Enter to generate a list of 100 random numbers.")
numbers = [random.randint(1, 100) for _ in range(25)]
print("-------------<<<<<<<<< GENERATED LIST >>>>>>>>>>>>>-----------------")
print(numbers)
print("<<<<<<<<------------------------------------------------>>>>>>>>>>>>")

# Find duplicates and display them
input("Press Enter to find duplicates and display them.")
duplicates = set([x for x in numbers if numbers.count(x) > 1])
print("------------<<<<<<<<< DUPLICATES LIST >>>>>>>>>>>>>-----------------")
print(duplicates)
print("<<<<<<<<------------------------------------------------>>>>>>>>>>>>")

# Remove duplicates and display the final list
input("Press Enter to remove duplicates and display the final list.")
unique_numbers = list(set(numbers))
print("--------------<<<<<<<<< UNIQUE LIST >>>>>>>>>>>>>-------------------")
print(unique_numbers)
print("<<<<<<<<------------------------------------------------>>>>>>>>>>>>")

# Shuffle the unique_numbers list to allow for a more random split
random.shuffle(unique_numbers)

# Divide the final list into two equal-sized lists
input("Press Enter to divide the final list into two equal-sized lists.")
mid = len(unique_numbers) // 2
list1 = unique_numbers[:mid]
list2 = unique_numbers[mid:]
print("-----------------<<<<<<<<< LIST 1 >>>>>>>>>>>>>---------------------")
print(list1)
print("-----------------<<<<<<<<< LIST 2 >>>>>>>>>>>>>---------------------")
print(list2)

# Calculate the sum of values for each list and determine the list with the higher sum
input("Press Enter to calculate the sum of values for each list.")
sum1 = sum(list1)
sum2 = sum(list2)

if sum1 > sum2:
    print("<<<<<<<<------------------------------------------------>>>>>>>>>>>>") 
    print("+++++++++++++++++<<< LIST 1 HAS THE HIGHER SUM. >>>+++++++++++++++++")
    print("<<<<<<<<------------------------------------------------>>>>>>>>>>>>")
elif sum2 > sum1:
    print("<<<<<<<<------------------------------------------------>>>>>>>>>>>>")
    print("+++++++++++++++++<<< LIST 2 HAS THE HIGHER SUM. >>>+++++++++++++++++")
    print("<<<<<<<<------------------------------------------------>>>>>>>>>>>>")
else:
    print("================<<< BOTH LISTS HAVE THE SAME SUM. >>>================")