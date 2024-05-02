

from lib import module_a
from lib.module_b import greet 
from lib.pkg_c.module_d import secret 
from lib.file_writer import writeToFile, readFromFile   
# calc = module_a.Calculator()
# result = f'Addition: {calc.add(10, 20)}' 
# print( result ) 
# greet() 
import json 

def fileDemo():
    print("Opening a new file") 
    writeToFile('data.txt', 'Hello, Python!')
    print( readFromFile('data.txt') ) 

def readJson():
    file = open('content.json', 'r') 
    data = file.read() 
    print( type(data)) 
    json_data = json.loads(data)
    print( type(json_data) )
    file.close() 

if __name__ == '__main__':
    # fileDemo() 
    readJson()