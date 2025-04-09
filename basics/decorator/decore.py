from datetime import datetime
import time

def logger(func):
    def wrapper():
        print("-"*50)
        print("Exection started at {}".format(datetime.today()))
        
        func()
        
        print("Exection started at {}".format(datetime.today()))
        print("-"*50)
        
    return wrapper

@logger        
def demo_function():
    print("Executing a task")
    time.sleep(3)
    print("Task Executed Successfully")
    

demo_function()