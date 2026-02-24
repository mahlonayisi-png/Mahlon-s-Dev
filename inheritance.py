class Mammal:
    def Walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("bark")
class Cat(Mammal):
    def annoying(self):
        print('annoying')


dog2 = Dog()
dog2.Walk()
