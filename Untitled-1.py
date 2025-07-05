class HelloWorld:
    def __init__(self,string):
        self.string = string
    def print_str(self)->None:
        print(self.string)
        
string = 'Hello World'

HelloWorld(string).print_str()
