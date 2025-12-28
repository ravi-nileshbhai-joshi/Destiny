with open("test.txt", "a") as file:
    file.write("Another line added\n")

with open("test.txt", "r") as file:
    content = file.read()

print("File now says:")
print(content)

