from models.__init__ import CURSOR, CONN

class AnimalFood:

    all = {}

    def __init__(self, fk_animal, fk_food, is_safe, id = None):
        self.id = id
        self.fk_animal = fk_animal
        self.fk_food = fk_food
        self.is_safe = is_safe #must be a string of true or false

    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, name):
    #     if isinstance(name, str) and 1 <= len(name):
    #         self._name = name
    #     else:
    #         raise Exception
    
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

    @classmethod
    def create(cls, fk_animal, fk_food, is_safe):
        """ Initialize a new AnimalFood instance and save the object to the database """
        animal_food = cls(fk_animal, fk_food, is_safe)
        animal_food.save()
        return animal_food