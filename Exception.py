try :
    num1 = eval(input("Enter a number: "))
    num2 = eval(input("Enter another number: "))

    div = num1 / num2
    print(f"Division is : {div:.2f}")
except ZeroDivisionError :
    print("Division by zero is not possible.")

except Exception as e :
    print("There is some error")
