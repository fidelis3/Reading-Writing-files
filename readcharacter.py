file = open('file.txt', 'r')

#If you want to read characters from a specific position in the file, you can use the seek() method. This method moves the file pointer (like a cursor) to a particular position.

file.seek(10)  # Move to the 11th byte (0-based index)

#To read specific characters, you can use the read() method with an argument that specifies the number of characters to read

characters = file.read(5)  # Read 5 characters from the current position
print(characters)

print(file.name)  # This will give you the name of the file you opened

file.close()
