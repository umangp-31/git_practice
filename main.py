# numbers = [1, 2, 3, 4, 5, 6]
#
# la = list(filter(lambda x: x%2!=0,numbers))
# ma = list(map(lambda x: x**2,la))
# print(ma)
#
# la=list(map(lambda x: x**2,filter(lambda x: x%2!=0,numbers)))
# print(la)
#
#
# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
# fact = reduce(lambda x, y: x*y, numbers)
# print(fact)


students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

sortl = sorted(students,key=lambda x:x["score"],reverse=True)
print(sortl)