# File processing library


def read_as_lines(file_path: str):
    file = open(file_path)
    contents = [line.rstrip() for line in file.readlines()]
    file.close()
    return contents


def write_as_lines(file_path: str, lines: ['stripped']):
    file = open(file_path, 'w')
    for each in lines:
        print(each, file=file)
    file.close()
