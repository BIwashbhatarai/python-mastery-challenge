def get_numbers():
    while True:
        try:
            first = float(input("Enter the first number: "))
            second = float(input("Enter the second number: "))
            return first, second
        except ValueError:
            print("Please enter valid numbers.")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# ... similarly update other operations ...

while True:
    ask = input("Do you want to use the calculator? (yes/no): ").lower()
    if ask != "yes":
        break
    print("Choose from below:")
    print("1) Add\n2) Subtract\n3) Divide\n4) Multiply\n5) Exponent\n6) Modulus")
    option = input("Choose (1/2/3/4/5/6): ")
    if option in ["1","2","3","4","5","6"]:
        first, second = get_numbers()
        if option == "1":
            print(add(first, second))
        elif option == "2":
            print(subtract(first, second))
        # ... rest of options ...
    else:
        print("Please choose correct option (1/2/3/4/5/6)")
