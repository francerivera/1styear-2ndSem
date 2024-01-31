name = str(input("Enter name: "))
if (name[-1].lower() in "aeiou"):
    age = int(input("Enter age: "))
    if age%2 == 0:
        print("Wow, you're special!")
    else:
        birth = int(input("Enter birth year: "))
        if birth%2 == 0:
            print("Oh, you're still special!")
        else:
            print("You will be special next year.")
else:
    print("You're awesome!")

