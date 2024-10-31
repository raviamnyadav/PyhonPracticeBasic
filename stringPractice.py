from datetime import date
from string import Template

name = "aman"
nameShort = name[0:3]
print("After slicing", nameShort)


# Slicing using skip
word = "amazing"
print(word[1::2])

# Function on string
print("The length of string :", len(name))
print("endswith n", name.endswith("n"))
print(name.startswith("a"))
print(name.capitalize())
print(name.upper())
print(name.lower())
count = name.count("a")
print(count)

a = "Aman is a very good boy \n but not a good boy \t boy"
print(a)


# Write a python program to display a user entered name by good afternoon using input function

string1 = input("Enter name :")
print("Good Afternoon", string1)
print(f"Dear {string1} \n you are selected \n {date.today()}")
print("Dear {} \n you are selected for an interview \n {}".format(name, date.today()))
print("Template string formate")
template = Template("My name is $name and I am $age years old.")
fromatted_string = template.substitute(name="Alice", age=30)
print(fromatted_string)


# write a program to detect double space in a string
input_string = "I am Aman Yadav  and testing for double space"

if "  " in input_string:
    print("Double space detected")
else:
    print("No double space detected")

# Replace the double space from the above question with single space.
if "  " in input_string:
    input_string_replace = input_string.replace("  ", " ")

print("Before replacing of all the double space ::::::", input_string)
print("After replacing of all the double space ::::::", input_string_replace)

#Write a program to format the following letter using escape sequence characters
letter = "Dear Aman, This the python course which you're practicing . Thanks!"
formatted_letter = "Dear Aman,\n This the python course which you're practicing.\n Thanks!"
print("Letter ::::::::")
print(letter)
print("Formatted letter ::::::::::::::::::")
print(formatted_letter)