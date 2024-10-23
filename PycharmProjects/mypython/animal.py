class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age


class Dog(Animal):
    def bark(self):
        print("a dog is barking")



class Bird(Animal):
    def fly(self):
        print("flying all day")



class Cat(Animal):
    def run(self):
        print("daniel's cat is running with me")


# dog = Dog("bob")
# dog.bark()
#
# bird = bird("diana")
# bird.fly()




