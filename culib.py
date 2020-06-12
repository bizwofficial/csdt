# UI library based on `uibase`


import uibase


get_handle = uibase.handle
clear_screen = uibase.cls


def welcome(main_program_version: str, hd: uibase.handle):
    uibase.title('Consoledit v{}'.format(main_program_version))
    hd.reset_screen_buffer_size()
    hd.free_focus(7, 35)
    print('Welcome to')
    hd.free_focus(8, 34)
    print('[Consoledit]')
    hd.free_focus(10, 33)
    print('Drag file here')
    hd.free_focus(11, 31)
    print('or enter file path')
    hd.free_focus(12, 36)
    print('to open')
    hd.free_focus(13, 31)
    print('Enter \'x\' to exit.')


def get_command():
    get_handle().clear_buffer(23)
    get_handle().focus(23)
    command = input('> ').rstrip()
    return command


def status_bar(anchor: int, buffers: [['stripped']]):
    get_handle().clear_buffer(24, page_end=True)
    get_handle().focus(24)
    get_handle().write('$$---{} screen of {}---$$'.format(anchor+1, len(buffers)).rstrip())


def custom_status_bar(text: str):
    get_handle().clear_buffer(24, page_end=True)
    get_handle().focus(24)
    get_handle().write(text)


def analysis_command(command: str, buffer_length: int):
    if command.isdigit():
        if len(command) == 2 and 1 <= int(command) <= buffer_length:
            buffer_number = int(command) - 1
            return 'edit', buffer_number
        else:
            return 'invalid', 'Invalid line-number'
    elif command == 'i' and command.isdigit():
        if len(command) == 2 and 1 <= int(command) <= buffer_length:
            buffer_number = int(command) - 1
            return 'insert', buffer_number
        else:
            return 'invalid', 'Invalid line-number'
    elif command == 'r' and command.isdigit():
        if len(command) == 2 and 1 <= int(command) <= buffer_length:
            buffer_number = int(command) - 1
            return 'replace', buffer_number
        else:
            return 'invalid', 'Invalid line-number'
    elif command == 's':
        return 'save',
    elif command in ['w', 'd']:
        return 'scroll', command
    elif command == 'x':
        return 'exit',
    else:
        return 'invalid', 'Invalid command'


def show_buffer(buffer: ['stripped']):
    for i, each in enumerate(buffer):
        get_handle().clear_buffer(i)
        get_handle().focus(i)
        line_number = i + 1
        if line_number < 10:
            buffer_number = '0' + str(line_number)
        else:
            buffer_number = str(line_number)
        print('<{}> '.format(buffer_number), end='')
        if len(each) >= 75:
            print(each[:72]+'...')
        else:
            print(each)


def clear_buffer():
    for i in range(20):
        get_handle().clear_buffer(i)


def dispatch_buffer(file_lines: ['stripped']):
    buffers = []
    for i, each in enumerate(file_lines):
        if i % 20 == 0:
            buffers.append([each])
        else:
            buffers[i//20].append(each)
    return buffers


def recover_buffer(buffers: [['stripped']]):
    lines = []
    for each in buffers:
        lines.extend(each)
    return lines


'''
h = get_handle()
welcome('0.1', h)
h.focus(23)
input('> ')
'''
