# 1. Accept numbers from a user
# NOTE: WAP to accept two numbers from the user and calculate multiplication

# Solution
num1 = int(input("Enter the first number:"))
num2 = int(input("Second the first number:"))

product = num1*num2
print("multiplication is:", product)

# 2. Display three string "NAME", "Is", "Danish" as "Name**Is**Danish"
# NOTE: Use the print() function to formate the given words in the mentioned format.
# Display the **separator between each string.

# Solution:
print('My', 'Name', 'Is', 'Danish', sep='*')

# 3. Convert Decimal number to octal using print() output formatting
''''
Given: num = 8
'''

# Solution
num = 8
print('%o'% num)

# 4. Display float number with 2 decimal places using print()
''''
Given:
num = 458.541315
'''

# Solution
num = 458.541315
print('%2f' % num)

# 5. Accept a list of 5 float numbers as an input from the user

# Solution
numbers = []
# 5 is the list size
# run loop 5 times
for i in range(0, 5):
    print('Enter number at location', i, ':')
    # accept float number from user
    item = float(input())
    # add it to the list
    numbers.append(item)

print('user list', numbers)

# 6. Write all content of a given file into a new file by skipping line number 5
''''
Given:

File:
line1
line2
.
.
.
line7
'''

# Solution
# Read test.txt
with open("C:\\Users\\DANISH\\Documents\\test.txt", 'r') as fp:
    # read all lines from a file
    lines = fp.readlines()

# open new file in write mode
    with open("C:\\Users\\DANISH\\Documents\\test.txt", 'w') as fp:
        count = 0
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1


# 7. Accept any three string from one input() call
# NOTE: WAP to take three names as input from a user in the single input() function call.

# Solution
str1, str2, str3 = input('enter three string').split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)


# 8. Formate variables using a string.format() method.
# NOTE: WAP to use string.format() method to format the following three variables.
''''
Given: totalMoney = 1000, quantity = 3, price = 450
'''
# Solution
''''  I have 1000 so i can buy 3 football for 450.00  '''
quantity = 3
totalMoney = 1000
price = 450
statement = 'i have {1} dollars so i can buy {0} football for {2:.2f} dollars'
print(statement.format(quantity, totalMoney, price))



# 9. Check file is empty or not
# NOTE: WAP to check if the given file is empty or not

# Solution
import os
size = os.stat('test.txt').st_size
if size == 0:
    print('file is empty')

# 10. Read line number 4 from the following files
''''
create a test.txt file and add the below content to it.
line1
.
.
.
line7
'''

# Solution

# read file
with open('test.txt', 'r') as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 3
    print(lines[2])


# COMPLETE