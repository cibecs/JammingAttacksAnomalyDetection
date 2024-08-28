class FileHandler: 
    # Read file and return data
    def __readFile (filename): 
        data = None
        with open(filename, 'r') as file: 
            data = file.read() 
            
        if data is None: 
            raise FileNotFoundError('File not found')
        
        return data
    def __parseData (data): 
        parsedData = []
        for line in data.split('\n'): 
            parsedData.append(float(line))
        return parsedData

    def readAndParseFile (filename): 
        data = FileHandler.__readFile(filename)
        return FileHandler.__parseData(data)   