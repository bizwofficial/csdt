# Line editor


import uibase


def edit_line(line: str, line_number: int):
    uibase.cls()
    print('Editing: {} line\n'.format(line_number))
    uibase.simulate_input(line)
    new_line = input().rstrip()
    return new_line


def replace_line(line: str, line_number: int):
    uibase.cls()
    print('Replacing: {} line\n'.format(line_number))
    new_line = input().rstrip()
    return new_line


def free_input(line_number: int):
    uibase.cls()
    print('Inserting lines to: {}line\n'.format(line_number))
    lines = []
    while True:
        try:
            lines.append(input().rstrip())
        except KeyboardInterrupt:
            break
    return lines
