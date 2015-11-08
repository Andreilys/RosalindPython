DNA = ""

newDNA = DNA[::-1]
newString = []

for index, char in enumerate(newDNA):
    if char == "T":
        newString.append("A")
    elif char == "A":
        newString.append("T")
    elif char == "C":
        newString.append("G")
    elif char == "G":
        newString.append("C")

print(''.join(newString))
