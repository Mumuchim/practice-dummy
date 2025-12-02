
# MUMUCHIM bracelet store

bracelet_wood = 30
bracelet_pearl = 2000
bracelet_diamond = 30000

tags = [bracelet_wood, bracelet_pearl, bracelet_diamond]
total = 0  # eto ang base
for price in tags:  # new for loop called "price" calling tags array
    total += price  # total base + current loop in array 1, then loop to array 2, then loop to array 3
print(f"Total: {total}")
