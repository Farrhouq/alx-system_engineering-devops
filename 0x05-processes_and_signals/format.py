import re
import sys


# handle trailing whitespace
def handle_trailing_space(line):
    if line is not None:
        return f"{line.rstrip()}\n"
    if line is not None:
        return line
    return ''


# handle tabs
def handle_tabs(line):
    new = re.sub(r'    ', '\t', line)
    if new is not None:
        return new
    return ''


# handle return brackets
def handle_return_brackets(line):
    line = line.rstrip()
    if "return" in line:
        line = line.rstrip(';')
        start_index = line.index("return")
        mini = line[start_index:].split()
        t = f"{mini[0]} ({' '.join(mini[1:])})"
        mini[1] = f"({mini[1]})"

        t = line[:start_index] + t
        if t is not None:
            return t + ';'
    return line


if __name__ == "__main__":
    FILENAME = sys.argv[1]
    with open(FILENAME, "r") as file:
        lines = file.readlines()
        file.close()
    with open(FILENAME, "w") as file:
        for line in lines:
            if line != '':
                line = handle_tabs(line)
                # line = handle_return_brackets(line)
                line = handle_trailing_space(line)
            file.write(line)
        if lines[-1] != '':
            file.write('')
        file.close()
    print(sys.argv[1], "is formatted")

