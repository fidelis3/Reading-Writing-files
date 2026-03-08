#open the file you want to read using the open() function.
file = open('file.txt', 'r')
#use readline() to read one line from the file at a time
line1 = file.readline()  # Reads the first line
line2 = file.readline()  # Reads the second line
#You can do things with each line you read. For example, you can print it, check if it contains specific words, or save it somewhere else.
print(line1)  # Print the first line
if 'python' in line2:
    print('This line is important!')
    
#you use a loop to read lines until no more lines are left. t's like reading the entire book, line by line.    
while True:
    line = file.readline()
    if not line:
        break  # Stop when there are no more lines to read
    print(line)
    
    
    
file.close()       
    