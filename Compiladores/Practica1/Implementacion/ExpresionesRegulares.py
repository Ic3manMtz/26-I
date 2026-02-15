import re

file = open("Factorial.java", mode='r')
archivo = file.read()

print("\n\nPatron:[a-z]")
x = re.findall("[a-z]", archivo)
print(x)

print("\n\nPatron:[a-z][a-z]")
x = re.findall("[a-z][a-z]", archivo)
print(x)

print("\n\nPatron:[a-z]+")
x = re.findall("[a-z]+", archivo)
print(x)

print("\n\nPatron:[A-Z][a-z]+")
x = re.findall("[A-Z][a-z]+", archivo)
print(x)

print("\n\nPatron:[A-Za-z][A-Za-z0-9]*")
x = re.findall("[A-Za-z][A-Za-z0-9 ]*", archivo)
print(x)

print("\n\nPatron:<=|>=|<|>")
x = re.findall("<=|>=|<|>", archivo)
print(x)

file.close()