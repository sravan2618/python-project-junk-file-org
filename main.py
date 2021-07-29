from orgbySize import orgbySize
from orgbyType import orgbyType

if __name__ == "__main__":

    PATH = input('Enter the absolute path of the directory : ')
    
    # move = orgbyType.orgbyType(PATH)
    # move.moveFiles()
    move = orgbySize(PATH)
    move.moveFiles()
    