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
    
    @classmethod
    def delete_animal(cls, name):
        sql = """
            DELETE FROM animals
            WHERE name = ?
        """

        CURSOR.execute(sql, (name,))
        CONN.commit()
        print(f"{name} deleted successfully")

        CONN.close()