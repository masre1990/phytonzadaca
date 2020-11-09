x=int(input("Upiši prvi broj: "))
y=int(input("Upiši drugi broj: "))

operation = input("Odaberi matematičku operaciju (+,-,/,*)")
if operation == "+":
    print(x+y)
elif operation == "-":
    print(x-y)
elif operation == "*":
    print(x*y)
elif operation == "/":
    print(x/y)
else:
    print("Neispravna matematička operacija")