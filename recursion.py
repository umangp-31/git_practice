#
# def fact(n):
#     if n == 0 :
#         return 1
#     else:
#         return n * fact(n-1)
#
# num = int(input("Enter a number: "))
# print(fact(num))



def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(6))