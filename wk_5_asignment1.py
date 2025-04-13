class Superhero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def use_power(self):
        print(f"{self.name} is using their {self.power} power!")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage. Remaining health: {self.health}")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Health: {self.health}")

class Batman(Superhero):
    def __init__(self, name="Batman", power="Martial Arts", health=100, gadgets=None):
        super().__init__(name, power, health)
        self.gadgets = gadgets if gadgets else []

    def use_gadget(self, gadget):
        if gadget in self.gadgets:
            print(f"{self.name} is using {gadget}!")
        else:
            print(f"{self.name} doesn't have {gadget}.")

    def display_info(self):
        super().display_info()
        print(f"Gadgets: {', '.join(self.gadgets)}")

class Superman(Superhero):
    def __init__(self, name="Superman", power="Flight", health=150, speed=None):
        super().__init__(name, power, health)
        self.speed = speed if speed else "Faster than a bullet"

    def display_info(self):
        super().display_info()
        print(f"Speed: {self.speed}")

# Create objects
batman = Batman(gadgets=["Batarang", "Grappling Hook"])
superman = Superman()

# Use methods
batman.use_power()
batman.use_gadget("Batarang")
batman.take_damage(20)
batman.display_info()

print()

superman.use_power()
superman.take_damage(30)
superman.display_info()