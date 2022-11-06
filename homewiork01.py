class Person:
    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job
    def __str__(self):
        return f'{self.name}, {self.age}, {self.job}'

Artur = Person('Artur',25,'Teacher')

class Monkey:
    max_age = 12
    loves_bananas = True

    def climb(self):
        print('I am climbing the tree') 

    
young = Monkey ()
old = Monkey ()

print (young.max_age,young.loves_bananas)
print (old.max_age,old.loves_bananas)
print (young.climb())
print (old.climb())


# x =12
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = name
        self.gender = gender
        
    def calculate_age (self,num):
        self.num = num 
    def __str__(self):
        return f'через {self.num} лет, будет {self.age + self.num} лет'        
Aliya = Person('Aliya',23,'female')

print (Aliya)    
Aliya.calculate_age(23)
print (Aliya)

import unittest
from rectangles import Rectangle

class TestCubes(unittest.TestCase):
    def test_init(self):
        c = Rectangle(5, 3, 10)
        self.assertEqual(c.length, 5)
        self.assertEqual(c.width, 3)
        self.assertEqual(c.height, 10)
    def test_init_raise(self):
        with self.assertRaises(ValueError):
            c = Rectangle('length', (1, 2, 3), {4: 5})

    def test_negative_value(self):
        with self.assertRaises(ValueError) as context:
            c = Rectangle(-1, 2, 6)

    def test_volume_calculation(self):
        c = Rectangle(5, 4, 7)
        self.assertEqual(c.calculate_volume(), 140)


class Reactangle:
    def __init__(self,length,width,height):
        if int (length) < 0 or int (width) <0  or int(height) <0:
            raise ValueError()
        self.length = length
        self.width = width
        self.height = height
        
def calculate_volume(self):
    return self.length * self.width * self.height














