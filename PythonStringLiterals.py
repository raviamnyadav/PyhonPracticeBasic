# importing all the libraries which is necessary
import time


# String literals in python print the statement are primarly used to format or design how specific string appear when printed
print("IQBEE website \n is the best website for staying up to date")

# Python "end" parameter in print()

# This line will automatically add a new line before the
# next print statement
print("IQBEE is for student professinals and has the best quality of content")

# This print will end with some character like "**" as set in the end argument
print("IQBEE is the best knowledgeable website for everyone", end="**")
print("Welcome to IQBEE")

# Print concatenated string
print("IQBEE is made by " + "Aman Yadav " + "Currently he is working on that website")

# Output formatting to make our statement more attractive by using str.format()
a, b = 10, 10000
print('The value of a is {} and the value of b is {}'.format(a, b))

# Python Input : we are using python input(). in python to take user input and print it in an output
n = input("Enter the values:")
print("Value which is provided by the user :", n)
print(type(n))


# Flush parameter in python with print() funciton
# suppose we want to show countdown in any platform so it will be slow if we dont't write in chuck format 
# For example
#with out flush
print("Output withour flush fucntion")
count_second = 10
for i in reversed(range(count_second + 1)):
    if i> 0:
        print(i, end='>>>')
        time.sleep(1)
    else :
        print('Start')


# with flush
print("Output with flush function")
count_second1 = 10
for i in reversed(range(count_second1 + 1)) :
    if i> 0:
        print(i, end='>>>', flush=True)
        time.sleep(1)
    else :
        print('Start')