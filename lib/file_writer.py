


def writeToFile( file_path, data ):

    file = open( file_path , 'w')  
    file.write( data ) 
    file.close() 
    return True 


def readFromFile( file_path ):

    file = open( file_path, 'r' ) 
    data = file.read() 
    return data 
