# "How can I implement a method to calculate a pet’s age in human years?"
# "What's the best way to retrieve a value from a dictionary in Python?"


class Pet:
    species_lifespan = {
        "dog": 13,
        "cat": 15,
        "rabbit": 9
    }
    
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def age_in_human_years(self):
        if self.species == "dog":
            return self.age * 7
        elif self.species == "cat":
            return self.age * 6
        elif self.species == "rabbit":
            return self.age * 5
        else:
            return self.age * 5
    
    def get_average_lifespan(self):
        return self.species_lifespan.get(self.species, "Unknown lifespan")

pet1 = Pet("Buddy", 3, "dog")
pet2 = Pet("Whiskers", 2, "cat")
pet3 = Pet("Thumper", 4, "rabbit")

print(f"{pet1.name} Human Age: {pet1.age_in_human_years()}, Lifespan: {pet1.get_average_lifespan()} years")
print(f"{pet2.name} Human Age: {pet2.age_in_human_years()}, Lifespan: {pet2.get_average_lifespan()} years")
print(f"{pet3.name} Human Age: {pet3.age_in_human_years()}, Lifespan: {pet3.get_average_lifespan()} years")
