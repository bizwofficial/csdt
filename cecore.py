# The core part of Consoledit


import culib
import cflib
import uibase
import celib


read = cflib.read_as_lines
save = cflib.write_as_lines


def save_from_buffers(file_path: str, buffers: [['stripped']]):
    lines = culib.recover_buffer(buffers)
    save(file_path, lines)


def read_as_buffers(file_path: str):
    file_lines = read(file_path)
    buffers = culib.dispatch_buffer(file_lines)
    return buffers


def loop(file_path: str):
    lines = [each.rstrip() for each in read(file_path)]
    buffers = culib.dispatch_buffer(lines)
    anchor = 0
    while True:
        culib.clear_screen()
        culib.show_buffer(buffers[anchor])
        culib.status_bar(anchor, buffers)
        cmd = culib.analysis_command(culib.get_command(), len(buffers[anchor]))
        if cmd[0] == 'exit':
            culib.custom_status_bar('Consoledit exited. Press any key to continue')
            uibase.pause()
            return
        elif cmd[0] == 'save':
            save_from_buffers(file_path, buffers)
        elif cmd[0] == 'scroll':
            if cmd[1] == 'w':
                if anchor != 0:
                    anchor -= 1
            else:
                if anchor != len(buffers) - 1:
                    anchor += 1
            continue
        elif cmd[0] == 'invalid':
            culib.custom_status_bar(cmd[1])
            uibase.pause()
        elif cmd[0] == 'edit':
            new_line = celib.edit_line(buffers[anchor][cmd[1]], cmd[1] + 1)
            buffers[anchor][cmd[1]] = new_line
            save_from_buffers(file_path, buffers)
        elif cmd[0] == 'replace':
            new_line = celib.replace_line(buffers[anchor][cmd[1]], cmd[1] + 1)
            buffers[anchor][cmd[1]] = new_line
            save_from_buffers(file_path, buffers)


loop('test.txt')
uibase.pause()
