

from FileHandler import FileHandler

def main():
    filename = 'data/constant_jammer.txt'
    data = FileHandler.readAndParseFile(filename)
    print(data)









if __name__ == '__main__':
    main()