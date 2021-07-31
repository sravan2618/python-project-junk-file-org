import os
from orgbySize import orgbySize
from orgbyType import orgbyType
from orgbyDate import orgbyDate

if __name__ == "__main__":

    print('-'*50)
    print(' '*8 + 'Welcome to the Junk File Organizer')
    print('-'*50)
    print('\n')
    PATH = input('Enter the full path of the folder : ')
    while not os.path.isdir(PATH):
        print('Invalid path')
        PATH = input('Enter the full path of the folder : ')
    print('\n')
    print('Select any one of the following organizing methods')
    print('By Type - [T]\nBy Size - [S]\nBy Date - [D]')
    print('\n')
    org_method = input('Enter the organizing method : ')
    caps_org_method = org_method.upper()
    while caps_org_method not in ('T','S','D'):
        print('Invalid method, Please try again')
        org_method = input('Enter the organizing method : ')
    print('\n')

    if caps_org_method == 'T':
        move = orgbyType(PATH)
        move.moveFiles()
    elif caps_org_method == 'S':
        move = orgbySize(PATH)
        move.moveFiles()
    elif caps_org_method == 'D':
        move = orgbyDate(PATH)
        move.moveFiles()

    print('Done!')
    