# 1. WAP a program to ask user to enter their favorite movies name
movies = []

# Entering movies name
for i in range(1, 4):
    movies_name = input(f"Enter your favorite movies name {i}")
    movies.append(movies_name)

# Display all the movies name which is entered by users
print("Your favorite movies :")
for movie in movies:
    print(movie)

print("Movies is the form of list :", movies)

# 2. WAP program to check wheather a list contains a palidrome of elements (hint use copy() methods)
original_list = [1, 2, 3, 2, 1]
copied_list = original_list.copy()
copied_list.reverse()

if original_list == copied_list:
    print("Pallindrome")
else:
    print("Not pallindrome")


# 3. WAP a program to count the number of students who got 'A' marks in the test
student_grade = ["A", "B", "A", "D", "C", "A"]
print("Number of students who got grade A in the exam are :", student_grade.count("A"))

# 4. WAP a program to sort above list in an ascending order
student_grade.sort()
print("After sorting the list become :", student_grade)
# removing duplicate while maintaing the order
unique_student_grade = []
[
    unique_student_grade.append(item)
    for item in student_grade
    if item not in unique_student_grade
]
print("After removing all the duplicate values", unique_student_grade)
