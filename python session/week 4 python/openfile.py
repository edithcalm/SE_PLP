# Step 1: Create the input file and write 5 lines of text into it
with open("input.txt", "w") as file:
    file.write("Learning Python is fun and easy.\n")
    file.write("File handling is a powerful concept.\n")
    file.write("We can read, write, and modify files.\n")
    file.write("Practice helps in mastering Python skills.\n")
    file.write("This is the fifth line of this file.\n")

# Step 2: Read the contents of input.txt
try:
    with open("input.txt", "r") as file:
        content = file.read()  # Read all the text from the file
except FileNotFoundError:
    print(" Error: 'input.txt' not found.")
    exit()
except IOError:
    print(" Error: Cannot read 'input.txt'.")
    exit()

# Step 3: Count the number of words
# Splitting the content by whitespace gives us all words
word_count = len(content.split())

# Step 4: Convert all text to uppercase
uppercase_content = content.upper()

# Step 5: Write the processed text and word count to output.txt
try:
    with open("output.txt", "w") as file:
        file.write("=== PROCESSED TEXT ===\n")
        file.write(uppercase_content + "\n")
        file.write(f"WORD COUNT: {word_count}\n")
except IOError:
    print(" Error: Could not write to 'output.txt'.")
    exit()

# Step 6: Print success message
print(" Success! Processed text and word count have been saved to 'output.txt'.")
