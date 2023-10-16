#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.Pet import Pet
from models.Foods import Foods
from models.Owner import Owner

def seed_database():
    Pet.drop_table()
    Pet.create_table()
    Foods.drop_table()
    Foods.create_table()
    Owner.drop_table()
    Owner.create_table()
    

    # Create seed data

    # Owner seed data
    cooper = Owner.create("cooper", "chris_Sm3ll$", "Ivy")
    kiki = Owner.create("kiki", "w1%CHing_H0ur", "Jiji")

    # Pet seed data
    Pet.create("Ivy", "dog", "cooper", ["sweet potatoes", "dog food"], ["chocolate"])
    Pet.create("Jiji", "cat", "kiki", ["sweet potatoes"], ["chocolate", "dog food"])
