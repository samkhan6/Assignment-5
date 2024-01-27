#Metaclass for Multiple Inheritance
class MultipleInheritanceMeta(type):
    def __new__(cls, name, bases, dct):
        if len(bases) > 1:
            raise ValueError(f"Class '{name}' cannot inherit from multiple classes.")
        return super().__new__(cls, name, bases, dct)

# Example usage:
class Base1:
    pass

class Base2:
    pass

class InvalidClass(Base1, Base2, metaclass=MultipleInheritanceMeta):
    pass  # This will raise a ValueError during class creation
