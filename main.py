num = int(input("Enter number"))
try:
    if num%2==0:
        print("Even number")
    else:
        print("Odd number")
except Exception as e:
    print(e)