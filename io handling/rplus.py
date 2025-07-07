with open('data.txt', 'r+') as file:
    file.write("Fresh line.....")
    file.seek(0)
    print(file.read())
    