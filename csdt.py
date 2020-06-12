# Main program. Run via double-clicking or command line.


try:
    import cecore
except Exception as err:
    import os
    import sys
    os.system('@title Consoledit [Safe Mode]')
    print('[Safe Mode]')
    print('Technical Information:\n', err, sep='\t')
    print('This error happened may because some important files are missing. Do you want to repair now?')
    print('Y = yes\nN = no')
    signal = True
    while signal:
        command = input('> ').rstrip().upper()
        if command in ['Y', 'N']:
            signal = False
        else:
            print('Invalid input.')
    if command == 'Y':
        print('Please wait a moment while installing the missing package...')
        os.system('python -m pip install pywin32 -i https://pypi.tuna.tsinghua.edu.cn/simple')
        print('\n\nRepair finished. Restart Consoledit to apply the changes.')
        os.system('pause')
        os.system('start python '+sys.argv[0])
    else:
        print('Maybe restarting Consoledit can solve this problem.')
        os.system('pause')
    exit()


VERSION = '0.1'
