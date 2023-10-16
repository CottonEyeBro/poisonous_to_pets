from models.__init__ import CURSOR, CONN
from models.Owner import Owner

class Pet:

    all = []

    def __init__(self, name, species, owner, safe_foods, unsafe_foods, id = None):
        self.id = id
        self.name = name
        self.species = species
        self.owner = owner
        self.safe_foods = safe_foods
        self.unsafe_foods = unsafe_foods

        Pet.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name):
            self._name = name
        else:
            raise Exception
        
    @property
    def species(self):
        return self._name
    
    @species.setter
    def species(self, species):
        if isinstance(species, str) and 1 <= len(species):
            self._species = species
        else:
            raise Exception
    
    def remove_pet(self):
        pass

    def update_pet(self):
        pass

    # def view_pet(self):
    #     print(f"Say 'Hello!' to {self.name}:\nSpecies: {self.species}\nOwner: {self.owner}\nSafe Foods: {self.safe_foods}\nUnsafe Foods: {self.unsafe_foods}\n")