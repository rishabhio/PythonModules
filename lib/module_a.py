



class Calculator:
    def __init__(self):
        pass 


    def add(self, a, b ):
        return a + b 
    
    def sub(self, a, b):
        return a - b 
    

    def mul(self, a, b):
        return a * b 
    
    def div(self, a, b):
        try:
            return a / b 
        except Exception as e:
            return 'Division by zero is not allowed'
        

    
if __name__ == '__main__':
    calci = Calculator() 
    print( calci.mul(10, 20) )
