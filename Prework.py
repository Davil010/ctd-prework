
# This program asks for a person's name and age and checks if they are old enough to drink in the US.

name = input("What is your name? ")
age = int(input("How old are you? "))

print("Hello", name, "you are", age, "years old.")

if age >= 21:
    print("You are old enough to drink.")
else:
    print("You are NOT old enough to drink. You must be 21!")