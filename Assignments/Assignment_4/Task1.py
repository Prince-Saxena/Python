
try:
    with open('sample.txt', 'r') as file:
        lines = file.readlines()
        line = 1
        for i in lines:
            print("Line",line,":",i)
            line += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' not found.")