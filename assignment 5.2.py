#Q3: Attribute Validation Metaclass
class AttributeValidationMeta(type):
    def __new__(cls, name, bases, dct):
        for key, value in dct.items():
            if isinstance(value, int):
                if value < 0:
                    raise ValueError(f"Attribute '{key}' must be a non-negative integer.")
        return super().__new__(cls, name, bases, dct)

# Example usage:
class ValidatedClass(metaclass=AttributeValidationMeta):
    age = 25  # This is valid
    invalid_age = -5  # This will raise a ValueError during class creation