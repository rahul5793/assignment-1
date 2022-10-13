from tokenize import Name


Name=input("Enter name:")
for char in range(len(Name) -1, -1, -1):
    print(Name[char], end="")
print("\n")

