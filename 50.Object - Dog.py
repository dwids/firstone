# OO from Lynda.com
class Dog():
    def __init__(self, name, age):   # class must have __init__ and self
        self.name = name
        self.age = age

    def bark(self):  # a simple method (like a function)
        print("Woof Woof!")

    def namebark(self):  # use your own data attribute in the method   DS added this
        print(self.name, "says: Woof Woof!")

    def yearsbark(self):   # bark once for each year of your age.  DS added this
        print("I am", self.name, "and I am:", self.age)
        # python loops like this one, don't do the 'final' number
        for i in range(1, self.age+1):
            print("Woof! for year", i)


fido = Dog("Fido", 2)
fido.bark()
#
print(fido.name)
print(fido.age)
fido.yearsbark()
# A year later we can check again
fido.age += 1  # shorthand for increment by 1
print("One year later...")
fido.yearsbark()
