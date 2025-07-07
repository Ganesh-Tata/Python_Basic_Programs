with open('data.txt','r') as file:
    lines= file.readlines()
    print("lines listt:", lines)
    print(file.closed)
    file.close()
    print(file.closed)

