a = float(input("1 число "))
b = float(input("2 число "))
option = input("Действие ")

if option == "+":
    print(a + b)
elif option == "-":
    print(a - b)
elif option == "*":
    print(a * b)
elif option == "/" and b != 0:
    print(a / b) 
else:
    print(None)