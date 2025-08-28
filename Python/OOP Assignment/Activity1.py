# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")
    
    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")


# Subclass with inheritance + polymorphism
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, waterproof):
        super().__init__(brand, model, storage)
        self.waterproof = waterproof
    
    # Polymorphism (overriding method)
    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Waterproof: {self.waterproof}")


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", 256)
watch1 = Smartwatch("Apple", "Watch Ultra", 32, True)

# Test methods
phone1.call("0712345678")
phone1.info()

watch1.call("0798765432")
watch1.info()
