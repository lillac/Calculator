a = float(input("1st Number:"))
b = float(input("2nd NUmber:"))
m = input("Enter m for *, d for /, s for -, a for +.")
c = a * b
y = a / b
f = a + b
h = a - b
if m == "m":
  print(c)
elif m == "d":
  print(y)
elif m == "s":
  print(h)
elif m == "a":
  print(f)
else:
  print("Error")
