# Renee Guldi
# SDEV220 - Python
# Prof. Chris Francis
# February 14, 2024

class guitar:
    def __init__(self, brand, model, num_strings, color):
        self.__brand = brand
        self.__model = model
        self.__num_strings = num_strings
        self.__color = color

    def get_brand(self):
        return self.__brand
    
    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model 
    
    def set_model(self, model):
        self.__model = model

    def get_num_strings(self):
        return self.__num_strings
    
    def set_num_strings(self, num_strings):
        self.__num_strings = num_strings

    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color

    def __str__(self):
        return f"A {self.__color} {self.__brand} {self.__model} with {self.__num_strings} strings."
    
    def __eq__(self, other):
        return (isinstance(other, guitar)) and self.__brand == other.get_brand() and self.__model == other.get_model() and self.__num_strings == other.get_num_strings() and self.__color == other.get_color()