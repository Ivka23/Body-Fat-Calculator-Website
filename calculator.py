import math

class Person:
    def __init__(self,age:int,gender:int,height:float,weight:float) -> None:
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
    
    def bmi (self)-> float:
        return self.weight