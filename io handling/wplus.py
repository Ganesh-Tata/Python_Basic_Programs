with open('data.txt', 'w+') as file:
    file.write("Hello, World!!! \n")
    file.write("This is a test file.\n")
    file.write("Appending a new line.\n")
    file.write("Final line.\n")
    file.seek(0)
