# using format function
amount = 153.746
print("Amount : RS {:.2f}".format(amount))


# using sep and end parameter
# end parameter with '@'
print("Python", end="@")
print("GeekforGeeks")

# separating with comma
print("Seprating with comma :", "G", "F", "G", sep="")

# for formatting date
print("09", "12", "2006", sep="-")

# Using f string
name = "Aman"
age = 23
print(f"hello, my name is {name} and I am {age} year old")

# using % which is similar to printf function in programming c
# %d = integer
# %f = float
# %s = string
# %x = hexadecimal
# %o = octal
num = float(input("Enter the value :"))
add = num + 5.5
print("The sum of the number is : %d" % add)


# we can take multiple input from the user in a single line using split function
x, y = input("Enter the values :").split()
print("Number of boys :", x)
print("Number of girls :", y)
boys = int(x)  # type casting the data type
girls = int(y)  # type casting the data type
student = boys + girls
print("Total number of students", student)


# taking conditional input from the user
age_input = input("Enter the age :")

# converting the input
age = int(age_input)

# checking condition based on the input
if age < 0:
    print("Please enter the valid age :")
elif age < 18:
    print("Minor age")
elif age >= 18 and age <= 65:
    print("You are adult")
else:
    print("You are in oldage")
