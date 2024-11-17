# Python list are contains to store set of values of any data types
friends = [
    "Ajay",
    "Rahul",
    "Tapadipta",
    "Raju",
    "Ashish",
    "Neha",
    "Nishu",
    "Sandhya",
    "Kiran",
    "Bhumi",
]

# List index :- can be index just like a string
print(friends[5])
print(friends[1])

# List methods
"""
list.sort() : Update the list in sorted manner
list.reverse() : update the list in reverse order
list.append(8) : add new element at the last 
list.insert(index, value) : add element in specified index
list.pop(index) : delete the what ever value will be there in the that particular index and return the value
list.remove(value) : It will remove the value which is given by the user
"""

list1 = [5,6,7,8,1,3,2,4,9,0]
print("The sorted array :", list1.sort())
print("The reverse array :", list1.reverse())
print("After appending :", list1.append(11))
print("After inserting :", list1.insert(3, 12))
print("Pop up methods in list :", list1.pop(0))

# Tuple
tup = (1, 2, 5, 4, 5)
print("Index number where  :", tup.index(1)) #return index of first occurance
print("Number of occurance :", tup.count(5)) #count total number of occurance


