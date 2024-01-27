#Q1: Logging Metaclass
class LoggingMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f"Initializing class: {name}")
        super().__init__(name, bases, dct)

# Example usage:
class MyClass(metaclass=LoggingMeta):
    pass
