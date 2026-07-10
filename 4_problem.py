# Q4 Write a program to input your age and display:
#  I am <age> years old.
#  (Use type casting while concatenating.) 

age = input("Enter your Age: ")
print("I am ",age,"years old.")

print(type(age))

print("_"*30)
#type casting
new_age = int(age)

print("I am ",new_age,"years old.")

print(type(new_age))