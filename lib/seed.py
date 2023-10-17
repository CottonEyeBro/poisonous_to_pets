#!/usr/bin/env python3
import sqlite3

from models.__init__ import CONN, CURSOR
# from models.Pet import Pet
# from models.Owner import Owner
from models.Animal import Animal
from models.Food import Food
from models.AnimalFood import AnimalFood

def seed_database():
    # Pet.drop_table()
    # Pet.create_table()
    # Food.drop_table()
    # Food.create_table()
    # Owner.drop_table()
    # Owner.create_table()
    

    # Create seed data

    # # Owner seed data
    # cooper = Owner.create("cooper", "chris_Sm3ll$", "Ivy")
    # kiki = Owner.create("kiki", "w1%CHing_H0ur", "Jiji")

    # # Food seed data
    # # chocolate = Food.create("chocolate", ["dog", "cat"], ["None"])
    # # sweet_potatoes = Food.create("sweet potatoes", ["None"], ["dog", "cat"])

    # # Pet seed data
    # Pet.create("Ivy", "dog", "cooper", ["sweet potatoes", "dog food"], ["chocolate"], cooper.id)
    # Pet.create("Jiji", "cat", "kiki", ["sweet potatoes"], ["chocolate", "dog food"], kiki.id)

    Animal.drop_table()
    Animal.create_table()
    Food.drop_table()
    Food.create_table()
    AnimalFood.drop_table()
    AnimalFood.create_table()

    #create objects
    dog = Animal.create("dog")
    cat = Animal.create("cat")

    chocolate = Food.create("chocolate")
    sweet_potatoes = Food.create("sweet potatoes")

    dog_chocolate = AnimalFood.create(dog.id, chocolate.id, "false")

seed_database()
