# manually closing a file: an exception could occur
# instead use a context manager as below
# will ensure the file is closed even if an exception is thrown

def open_file(filename):
    with open(filename) as f:
        f.write("hello!\n")
        
# dont use a bare except clause as except: ....
# instead catch the exception Exception, or the actual erroe

def bare_except():
    while True:
        try:
            s = input("Enter a number")
            x = int(s)
        except Exception: #or even better except ValueErroe
            print("Oops, not a number")
            
 
            
