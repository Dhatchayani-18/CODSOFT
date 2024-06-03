
print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")
option = int(input("Choose any one from: 1, 2, 3, 4 :"))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if option == 1:
    print(a+b)
elif option == 2:
    print(a-b)
elif option == 3:
    print(a*b)
elif option == 4:
    print(a/b)
else:
    print("Invalid input")
