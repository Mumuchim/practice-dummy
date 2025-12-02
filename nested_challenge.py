print("Mosh version: \n")

numbers = [5, 2, 5, 2, 2]
for loop in numbers:
    output = ""
    for count in range(loop):
        output += "x"
    print(output)

print("                 ")
print("Mumuchim version: \n")

for loop in numbers:
    x = "x"
    print(loop * x)
