import numpy as np

# Specify the path to the .dat file
file_path = 'cotton_v_total_exports.dat'

# Initialize lists to hold the columns
column1 = []
column2 = []
column3 = []

# Open the file and read line by line
with open(file_path, 'r') as file:
    # Skip the header line (first line of the file)
    next(file)  # This skips the first line (header)

    # Process each subsequent line
    for line in file:
        # Strip any surrounding whitespace and split by spaces or tabs
        parts = line.strip().split()

        # Convert each part to a float and append to the appropriate column
        column1.append(float(parts[0]))
        column2.append(float(parts[1]))
        column3.append(float(parts[2]))

# Convert lists to numpy arrays for easier manipulation (optional)
column1 = np.array(column1)
column2 = np.array(column2)
column3 = np.array(column3)

# Display the arrays
print("Column 1:", column1)
print("Column 2:", column2)
print("Column 3:", column3)

print(len(column1))

def percentage(i, j):
    return i/j * 100

percents = [column1, percentage(column3, column2)]

out_path = 'output.dat'
np.savetxt(out_path, percents, delimiter="\t", fmt='%.0f')