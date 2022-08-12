import sys
import re


def clean_line(line):
    line = re.sub(r'http\S+', '', line) # Remove links
    line = re.sub(r"@[^\" ]+", "", line) # Remove usernames
    line = re.sub(r'[^\w\s]', '', line) # Remove punctuation
    line = re.sub(r'[0-9]+', '', line) # Remove numbers
    line = re.sub(' +', ' ', line) # Remove whitespace
    line = line.lower()
    line = line.strip()

    return line

input = open(sys.argv[1], "r")
output = open(sys.argv[1] + ".clean", "w")

print(f"Input: {input}")
print(f"Output: {output}")

for line in input.readlines():
    new_line = clean_line(line)
    if (new_line):
        output.writelines(new_line + '\n')

input.close()
output.close()
