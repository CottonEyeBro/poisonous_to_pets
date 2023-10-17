from models.__init__ import CURSOR, CONN

class Owner:

    all = []

    def __init__(self, username, password, pets, id = None):
        self.id = id
        self.username = username
        self.password = password
        self.pets = pets

        Owner.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 1 <= len(username):
            self._username = username
        else:
            raise Exception
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, species):
        if isinstance(password, str) and 1 <= len(password):
            self._password = password
        else:
            raise Exception

    @property
    def pets(self):
        return self._pets

    @pets.setter
    def pets(self, pets):
        if isinstance(pets, list) and all(isinstance(pet, str) for pet in pets):
            self._pets = pets
        else:
            raise Exception
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Owner instances """
        sql = """
            CREATE TABLE IF NOT EXISTS owners (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            pets TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    # @classmethod
    # def drop_table(cls):
    #     """ Drop the table that persists Department instances """
    #     sql = """
    #         DROP TABLE IF EXISTS departments;
    #     """
    #     CURSOR.execute(sql)
    #     CONN.commit()

    def save(self):
        """ Insert a new row with the name and location values of the current Department instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO departments (name, location)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, location):
        """ Initialize a new Department instance and save the object to the database """
        department = cls(name, location)
        department.save()
        return department

    # def update(self):
    #     """Update the table row corresponding to the current Department instance."""
    #     sql = """
    #         UPDATE departments
    #         SET name = ?, location = ?
    #         WHERE id = ?
    #     """
    #     CURSOR.execute(sql, (self.name, self.location, self.id))
    #     CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Department instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM departments
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    # @classmethod
    # def instance_from_db(cls, row):
    #     """Return a Department object having the attribute values from the table row."""

    #     # Check the dictionary for an existing instance using the row's primary key
    #     department = cls.all.get(row[0])
    #     if department:
    #         # ensure attributes match row values in case local instance was modified
    #         department.name = row[1]
    #         department.location = row[2]
    #     else:
    #         # not in dictionary, create new instance and add to dictionary
    #         department = cls(row[1], row[2])
    #         department.id = row[0]
    #         cls.all[department.id] = department
    #     return department

    # @classmethod
    # def get_all(cls):
    #     """Return a list containing a Department object per row in the table"""
    #     sql = """
    #         SELECT *
    #         FROM departments
    #     """

    #     rows = CURSOR.execute(sql).fetchall()

    #     return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Department object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM departments
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Department object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM departments
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    # def employees(self):
    #     """Return list of employees associated with current department"""
    #     from models.employee import Employee
    #     sql = """
    #         SELECT * FROM employees
    #         WHERE department_id = ?
    #     """
    #     CURSOR.execute(sql, (self.id,),)

    #     rows = CURSOR.fetchall()
    #     return [
    #         Employee.instance_from_db(row) for row in rows
    #     ]
