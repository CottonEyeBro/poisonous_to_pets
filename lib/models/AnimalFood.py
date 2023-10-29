from models.__init__ import CURSOR, CONN

class AnimalFood:

    all = {}

    def __init__(self, fk_animal, fk_food, is_safe, id = None):
        self.id = id
        self.fk_animal = fk_animal
        self.fk_food = fk_food
        self.is_safe = is_safe # must be a string of true or false


    @property
    def fk_animal(self):
        return self._fk_animal
    
    @fk_animal.setter
    def fk_animal(self, fk_animal):
        if isinstance(fk_animal, int) and 0 <= fk_animal:
            self._fk_animal = fk_animal
        else:
            raise Exception
        
    @property
    def fk_food(self):
        return self._fk_food
    
    @fk_food.setter
    def fk_food(self, fk_food):
        if isinstance(fk_food, int) and 0 <= fk_food:
            self._fk_food = fk_food
        else:
            raise Exception
        
    @property
    def is_safe(self):
        return self._is_safe
    
    @is_safe.setter
    def is_safe(self, is_safe):
        if isinstance(is_safe, str) and (is_safe == "true" or is_safe == "false"):
            self._is_safe = is_safe
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of AnimalFood instances """
        sql = """
            CREATE TABLE IF NOT EXISTS animals_foods (
            is_safe TEXT,
            id INTEGER PRIMARY KEY,
            fk_animal INTEGER,
            fk_food INTEGER,
            FOREIGN KEY(fk_animal) REFERENCES animals(id),
            FOREIGN KEY(fk_food) REFERENCES foods(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists AnimalFood instances """
        sql = """
            DROP TABLE IF EXISTS animals_foods;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the foreign key values and safety data of the current AnimalFood instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO animals_foods (fk_animal, fk_food, is_safe)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.fk_animal, self.fk_food, self.is_safe))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        # print(AnimalFood.all)

    @classmethod
    def create(cls, fk_animal, fk_food, is_safe):
        """ Initialize a new AnimalFood instance and save the object to the database """
        animal_food = cls(fk_animal, fk_food, is_safe)
        animal_food.save()
        return animal_food


    
    # @classmethod
    # def instance_from_db(cls, row):
    #     """Return an AnimalFood object having the attribute values from the table row."""

    #     if row and len(row) >= 4:  # Check if row contains at least 4 elements
    #         # Check the dictionary for an existing instance using the row's primary key
    #         animal_food = cls.all.get(row[1])
    #         if animal_food:
    #             # Update the attributes
    #             animal_food.is_safe = row[0]
    #             animal_food.fk_animal = row[2]
    #             animal_food.fk_food = row[3]
    #         else:
    #             # If not found, create a new instance
    #             animal_food = cls(row[1], row[2], row[3])
    #             cls.all[animal_food.fk_food] = animal_food
    #         return animal_food
    #     else:
    #         print("Invalid row:", row)
    #         return None



    @classmethod
    def instance_from_db(cls, row):
        """Return an AnimalFood object having the attribute values from the table row."""
        print("Row:", row) 
        # Check the dictionary for an existing instance using the row's primary key
        animal_food = cls.all.get(row[1])
        if animal_food:
            # ensure attributes match row values in case local instance was modified
            animal_food.is_safe = row[0]
            animal_food.fk_animal = row[2]
            animal_food.fk_food = row[3]
        else:
            print("animal not found")
        return animal_food
    
    @classmethod
    def find_by_animal(cls, animal_name):
        from models.Animal import Animal
        """
        Find and return all food associations for a specific animal by its name.
        """
        animal = Animal.find_by_name(animal_name)
        if animal:
            CURSOR.execute("SELECT * FROM animals_foods WHERE id = ?", (animal.id,))
            rows = CURSOR.fetchall()
            return [cls(*row) for row in rows]
        else:
            return []

    @classmethod
    def find_by_id(cls, id):
        """Return a AnimalFood object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT id
            FROM animals_foods
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def delete_dictionary_entry(self, id):
        """Delete the dictionary entry corresponding to the current animal_food instance, and reassign id attribute"""

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def find_unsafe_by_id(cls, id):
        """Returns id of AnimalFood object if it is unsafe to eat"""
        sql = """
            SELECT * FROM animals_foods
            WHERE id = ?
            AND is_safe = "false"
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None