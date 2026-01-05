try:
    num = int(input("Enter number"))
    if num%2==0:
        print("Even number.")
    else:
        print("Odd number.")

except Exception as e:
    print("Something went wrong.")
