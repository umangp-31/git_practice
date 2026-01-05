try:
    num = int(input("Enter number : "))
    for i in range(1,11):
        print(f"{num} x {i} = {i*num}")
except Exception as e:
    print("Enter valid number")