# This library provides the basic UI operations.


import os
import win32console as wc
import win32api as wa
import win32con as wc1


key_mapping = {'!': (49, True), '@': (50, True), '#': (51, True),
               '$': (52, True), '%': (53, True), '^': (54, True),
               '&': (55, True), '*': (56, True), '(': (57, True),
               ')': (48, True), '-': (189, False), '_': (189, True),
               '=': (187, False), '+': (187, True), '[': (219, False),
               '{': (219, True), ']': (221, False), '}': (221, True),
               '\\': (220, False), '|': (220, True), ';': (186, False),
               ':': (186, True), '\'': (222, False), '"': (222, True),
               ',': (188, False), '<': (188, True), '.': (190, False),
               '>': (190, True), '/': (191, False), '?': (191, True),
               '`': (192, False), '~': (192, True), '\n': (13, False),
               ' ': (32, False), '\t': (9, False), '    ': (9, False)}


class doc_line:

    def __init__(self, line_number, text):                                       # Initialize instance with the line
        self.line_number = line_number                                           # number, the contents and the
        self.text = text                                                         # in-buffer line number.
        self.buffer_number = 0

    def set_buffer_number(self, buffer_number):                                  # Use when turning pages
        self.buffer_number = buffer_number

    def set_line_number(self, line_number):
        self.line_number = line_number

    def set_text(self, text):
        self.text = text


class handle:

    def __init__(self):
        self.hd = wc.GetStdHandle(wc.STD_OUTPUT_HANDLE)
        self.ihd = wc.GetStdHandle(wc.STD_INPUT_HANDLE)
        self.hd.SetConsoleCursorInfo(Size=100, Visible=True)

    def refresh_handle(self):
        self.hd = wc.GetStdHandle(wc.STD_OUTPUT_HANDLE)

    def reset_screen_buffer_size(self):                                          # Used when program starts
        self.hd.SetConsoleScreenBufferSize(wc.PyCOORDType(80, 25))

    def clear_buffer(self, buffer_number, page_end=False):                                       # Clear a specific line
        self.hd.SetConsoleCursorPosition(wc.PyCOORDType(0, buffer_number))
        if page_end:
            self.write(' '*79)
        else:
            self.write(' '*80)

    def focus(self, buffer_number):                                              # Move cursor to a specific line
        self.hd.SetConsoleCursorPosition(wc.PyCOORDType(0, buffer_number))

    def free_focus(self, row, column):                                           # Move cursor to a specific line&column
        self.hd.SetConsoleCursorPosition(wc.PyCOORDType(column, row))

    def write(self, text: str):
        self.hd.WriteConsole(text)

    def read_fake(self):
        self.ihd.ReadConsoleInput(1)


def simulate_input(char_list: str):                                        # Used in line editor
    for each in char_list:
        key = ord(each)
        if each.isupper():
            wa.keybd_event(16, 0, 0, 0)
            wa.keybd_event(key, 0, 0, 0)
            wa.keybd_event(16, 0, wc1.KEYEVENTF_KEYUP, 0)
        elif each.islower():
            key -= 32
            wa.keybd_event(key, 0, 0, 0)
        elif each.isdigit():
            wa.keybd_event(key, 0, 0, 0)
        else:
            key = key_mapping[each][0]
            if key_mapping[each][1]:
                wa.keybd_event(16, 0, 0, 0)
                wa.keybd_event(key, 0, 0, 0)
                wa.keybd_event(16, 0, wc1.KEYEVENTF_KEYUP, 0)
            else:
                wa.keybd_event(key, 0, 0, 0)


def cls():
    os.system('@cls')


def pause():
    handle().read_fake()


def title(tt: str):
    wc.SetConsoleTitle(tt)
