# ---------- Polymorphism in Python ----------

class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane(Bird):
    def fly(self):
        print("Airplane can fly")

# Polymorphism allows us to use the same method name for different classes and it will work based on the object that is calling the method. This is called method overriding.

obj1 = Bird()

obj1.fly() # calling the fly method using the object of the Bird class. This will call the fly method of the Bird class. If you use the object of the Airplane class to call the fly method, it will call the fly method of the Airplane class because of polymorphism.

