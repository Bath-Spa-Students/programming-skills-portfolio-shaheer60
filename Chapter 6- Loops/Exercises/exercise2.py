print("How old are you?")
print("enter 'quit' when you are finished.")

while True:
    ager = input()
    if age == 'quit':
        break
    age=int(age)

    if age < 3:
        print(" you get in free!")
    elif age < 13:
        print(" your ticket is $10.")
    else:
        print(" your ticket is $15.")