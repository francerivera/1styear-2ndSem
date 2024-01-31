while True:
    char = str(input("Enter a character: "))
    if char.lower() == "x":
        print(f"{char} "*3)
        break
    if char.isdigit():
        continue
    print(f"{char} "*3)