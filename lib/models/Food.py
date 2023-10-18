from models.__init__ import CURSOR, CONN

class Food:

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
        """ Create a new table to persist the attributes of Food instances """
        sql = """
            CREATE TABLE IF NOT EXISTS foods (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Food instances """
        sql = """
            DROP TABLE IF EXISTS foods;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name value of the current Food instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO foods (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """ Initialize a new Food instance and save the object to the database """
        food = cls(name)
        food.save()
        return food
    
    # Get all supported food function
    @classmethod
    def instance_from_db(cls, row):
        """Return a Food object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        food = cls.all.get(row[0])
        if food:
            # ensure attributes match row values in case local instance was modified
            food.name = row[1]
        else:
            # not in dictionary, create new instance and add to dictionary
            food = cls(row[1])
            food.id = row[0]
            cls.all[food.id] = food
        return food
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Food object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM foods
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_all_food(cls):
        """Return a list containing a Food object per row in the table"""
        sql = """
            SELECT *
            FROM foods
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]