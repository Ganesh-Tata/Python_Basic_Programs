with open('data.txt', 'w') as file:
    file.write("Hello, World!!! \n")
    file.write("This is a test file.\n")
    file.write("Appending a new line.\n")
    file.write("Final line.\n")   

with open('data.txt', 'a') as file:
    file.write("Appending this line to the existing file.\n")
    file.write("This line is added in append mode.\n")

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]        
with open('data.txt', 'w') as file:
    file.writelines(lines)

with open('data.txt', 'r') as file:
    data = file.read()
    print(data)
