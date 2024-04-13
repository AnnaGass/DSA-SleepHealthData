# Specify the file path
file_path = "data/subject7_stage.txt"  # Replace "your_file.txt" with the actual file path

# Initialize a line counter
line_count = 0

# Open the file and iterate over each line
with open(file_path, 'r') as file:
    for line in file:
        line_count += 1

print("Number of lines in the file:", line_count)