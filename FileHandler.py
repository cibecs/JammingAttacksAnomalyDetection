import numpy as np

class FileHandler: 
    # Read file and return data
    def __readFile (filename, maxLines): 
        data = []
        f = open(filename, 'r')

        for _ in range (maxLines):
            line = f.readline()
            if not line: 
                break
            data.append(line)

        if len(data) == 0: 
            raise FileNotFoundError('File not found or empty')
        
        return data
    def __parseData (data): 
        parsedData = []
        for line in data: 
            parsedData.append(float(line))
        return np.array(parsedData).reshape(-1,1)

    def readAndParseFile (filename, maxLines): 
        data = FileHandler.__readFile(filename, maxLines)
        return FileHandler.__parseData(data)   