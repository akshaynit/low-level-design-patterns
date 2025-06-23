from threading import Lock

'''
Class Logger is a singleton class where only single object of logger is created
even when the logger object is created multiple times in the code.
'''
class Logger:
    _instance = None   # class variable to store the single object instance
    _lock = Lock()     # lock object is also stored as class variable so that every call used same lock to lock the critical section

    def __new__(cls, *args):
        with cls._lock:
            if cls._instance == None:
                cls._instance = super().__new__(cls)
                cls._instance._is_instantiated = False
        return cls._instance

    def __init__(self, name):
        if not self._is_instantiated:
            self.name = name
            self._is_instantiated = True

logger_a = Logger("loggerA")
logger_b = Logger("loggerB")
logger_c = Logger("loggerC")

print(logger_c.name) # logger_c has name set to loggerA since the object is created only once
print(logger_a == logger_b == logger_c)  # check to verify the logger objects are actually same
