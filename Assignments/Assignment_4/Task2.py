text = input("Enter the text to write to file:")

file = open("output.txt",'w')
file.write(text)
file.close()
print("Data successfully written to 'output.txt'.")

text1 = input("Enter additional data to append:")

file1 = open("output.txt",'a')
file1.write(text1)
file1.close()

file3 = open('output.txt','r')
r = file3.read()
print("Final content of output.txt")
print(r)
file3.close()