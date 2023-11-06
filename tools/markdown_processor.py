import sys


def find_lines_starting_with_asterisk(lines):
    line_numbers = []
    for i, line in enumerate(lines):
        if line.startswith("* "):
            line_numbers.append(i + 1)
    return line_numbers


def find_sparse_diapasons(line_numbers):
    """
    Find sparse diapasons in a list of line numbers
    E.g. [9, 10, 11, 15, 17, 19, 23, 25] -> [(15, 19), (23, 25)]
    """
    sparse_diapasons = []
    i = 0
    sparse_diapason_begin = None
    while i < len(line_numbers):
        if sparse_diapason_begin is None and line_numbers[i + 1] - line_numbers[i] == 2:
            sparse_diapason_begin = line_numbers[i]
            i = i + 1
        elif sparse_diapason_begin is not None:
            # check end of list
            if i == len(line_numbers) - 1:
                sparse_diapasons.append((sparse_diapason_begin, line_numbers[i]))
                break
            elif line_numbers[i + 1] - line_numbers[i] == 2:
                i = i + 1
            else:
                sparse_diapasons.append((sparse_diapason_begin, line_numbers[i]))
                sparse_diapason_begin = None
                i = i + 1
        else:
            i = i + 1
    return sparse_diapasons


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input.md")
        sys.exit(1)

    md_file_path = sys.argv[1]
    with open(md_file_path, 'r') as file:
        lines = file.readlines()
    list_lines = find_lines_starting_with_asterisk(lines)
    print(f"Lines starting with * are: {list_lines}")

    sparse_diapasons = find_sparse_diapasons(list_lines)
    print(f"Sparse diapasons are: {sparse_diapasons}")

    lines_to_remove = []
    for start, end in sparse_diapasons:
        for i in range(start + 1, end, 2):
            lines_to_remove.append(i)

    print(f"Line numbers to be removed: {lines_to_remove}")

    # Remove the lines to be removed
    lines = [line for i, line in enumerate(lines) if i + 1 not in lines_to_remove]

    # Write the updated lines back to the file
    with open(md_file_path, 'w') as file:
        file.writelines(lines)

    print("Lines removed and updated in the file.")
