#check palindrome or not
a = input("enter string for check palindrome or not : ")
if a == a[::-1]:
    print("palindrome")
else:
    print("not palindrome")
