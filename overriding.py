class Animal:
    def speak(self):
        return "Woof"

class Dog(Animal):
    pass

class Cat(Animal):
    def speak(self):
        return "Meow!"

    
class Labro(Animal):
   pass

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()
labro = Labro()
# Call the overridden methods

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
print(labro.speak())  # Output: Meow!
