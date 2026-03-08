# Reading and Storing the Entire Content of a File

# Using the read method, you can retrieve the complete content of a file
# and store it as a string in a variable for further processing or display.

# Step 1: Open the file you want to read
with open('file.txt', 'r') as file:

    # Step 2: Use the read method to read the entire content of the file
    file_stuff = file.read()

    # Step 3: Now that the file content is stored in the variable 'file_stuff',
    # you can manipulate or display it as needed.

    # For example, let's print the content to the console:
    print(file_stuff)

# Step 4: The 'with' statement automatically closes the file when it's done,
# ensuring proper resource management and preventing resource leaks.