import os, json, time



def logger(func):
    def wrapper():
        print(f'Running {func.__name__}')
        func()
        print('Complete')
    return wrapper 

def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        print("--- %s seconds ---" % (time.time() - start_time))
    return wrapper 


def ask(prompt):
    print(prompt)
    return input('>')

def placeholder():
    print('This is a placeholder')




# file reading shit 

class file():
    def __init__(self, location) -> None:
        self.loc = location
        if self.loc == None:
            print('File location is not defined')
            pass
    
    def write(self, text):
        f = open(self.loc, "w")
        f.write(text)
        f.close()

    def append(self, text):
        f = open(self.loc, "a")
        f.write(text)
        f.close()

class read(file):
        def __init__(self, location) -> None:
            super().__init__(location)

        def read_line(self, loop: int=''):
            f = open(self.loc, "r")
            for i in loop:
                return f.readline()
            f.close()

        def loop_file(self):
            f = open(self.loc, "r")
            for x in f:
                return x
            f.close()
        
        def read_char(self, char):
            f = open(self.loc, "r")
            text = f.read(char)
            f.close()
            return

        def read_file(self):
            f = open(self.loc, "r")
            text = f.read()
            f.close()
            return text
        
# end of file reading shit 
        
        
