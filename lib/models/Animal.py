from models.__init__ import CURSOR, CONN
class Animal:

    all = {}

    def __init__(self, name, id = None):
        self.id = id
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name):
            self._name = name
        else:
            raise Exception
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Animal instances """
        sql = """
            CREATE TABLE IF NOT EXISTS animals (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Animal instances """
        sql = """
            DROP TABLE IF EXISTS animals;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name value of the current Animal instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO animals (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """ Initialize a new Animal instance and save the object to the database """
        animal = cls(name)
        animal.save()
        return animal


    ### DELETE ###

    def animal_foods_ids(self):
        """Return list of animals_foods associated with current animal"""
        from models.AnimalFood import AnimalFood
        sql = """
            SELECT id FROM animals_foods
            WHERE fk_animal = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        ids = []
        for tupl in rows:
            ids.append(tupl[0])
        return ids

    def delete_animal_foods(self, id):
        """Delete each row where an animal occurs in the AnimalsFoods table"""
        sql = """
            DELETE FROM animals_foods
            WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        CONN.commit()
        #AnimalFoods dictionary is not updated by this

    @classmethod
    def instance_from_db(cls, row):
        """Return an Animal object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        animal = cls.all.get(row[0])
        if animal:
            # ensure attributes match row values in case local instance was modified
            animal.name = row[1]
        else:
            # not in dictionary, create new instance and add to dictionary
            animal = cls(row[1])
            animal.id = row[0]
            cls.all[animal.id] = animal
        return animal

    @classmethod
    def find_by_name(cls, name):
        """Return an Animal object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM animals
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def delete(self, id):
        """Delete the table row corresponding to the current Animal instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM animals
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # from AnimalFood import update_dictionary
        # update_dictionary()

        # Set the id to None
        self.id = None
    

