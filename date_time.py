import datetime

d= datetime.datetime.now()

print(d)
print(f"YEAR : {d.strftime('%Y')}")
print(f"MONTH : {d.strftime('%B')}")
print(f"DAY : {d.strftime('%d')}")
