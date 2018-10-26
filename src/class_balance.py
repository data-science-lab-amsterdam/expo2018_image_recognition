import glob
import collections

# Get all the files
txt_files = glob.glob("image_labels_dir/*.txt")

# Function to read all lines of a file
def read_lines(file):
     with open(file, 'rt') as fd:
         first_line = fd.readlines()
     return first_line

# apply read lines function all text files
output_strings = map(read_lines, txt_files)

# Unlist list of lists (list of items per text file was returned)
output_strings = [item for sublist in output_strings for item in sublist]

# Count occurances
counter = collections.Counter(output_strings)
print(counter)