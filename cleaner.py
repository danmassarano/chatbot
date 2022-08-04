import re
import sys

input = open(sys.argv[1], "r")
output = open(sys.argv[1] + ".clean", "w")

print(f"Input: {input}")
print(f"Output: {output}")


def clean_line(line):
    # * remove things wrapped in brackets
    line = re.sub(r"\[\S+\]", "", line)
    line = re.sub(r"\(\S+\)", "", line)

    # * remove urls
    line = re.sub(r"http[^\" ]+\b", "", line)

    # * remove @<username>
    line = re.sub(r" @[^\" ]+\b", "", line)
    line = re.sub(r"^@[^\" ]+\b", "", line)
    line = re.sub(r"^\"@[^\" ]+\b", "", line)

    # * remove hashtags
    line = re.sub(r" #[^\" ]+\b", "", line)

    # * ellipsis
    line = re.sub(r"\.\.\.", "", line)

    # * remove non-printing unicode
    # TODO do we want this?
    # line = re.sub(r"[^ -~]+", "", line)

    return line


for line in input.readlines():
    new_line = clean_line(line)
    output.writelines(new_line)

input.close()
output.close()
