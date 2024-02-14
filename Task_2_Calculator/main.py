import Operation as Op
while True:
    operator = int(input("\nSelect operation of your choice: "
                         "\n1-Add\t2-Subtract\t3-Multiply\t4-Divide\t5-Exit\nSelection: "))
    if operator == 5:
        break
    elif operator > 4 or operator < 1:
        print("\nEnter valid choice.")
    else:
        num1 = input('Enter first number:')
        num2 = input('Enter second number:')
        result = Op.calculate(num1, operator, num2)
        print(f"\n{num1} {Op.operator_symbol(operator)} {num2} = {result}")
    print("___________________________________________________________________")
