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
    dog_sweet_potatoes = AnimalFood.create(dog.id, sweet_potatoes.id, "true")
    cat_chocolate = AnimalFood.create(cat.id, chocolate.id, "false")
    cat_sweet_potatoes = AnimalFood.create(cat.id, sweet_potatoes.id, "false")

    # dog
    dog_dog_food = AnimalFood.create(dog.id, dog_food.id, "true")
    dog_avocado = AnimalFood.create(dog.id, avocado.id, "false")
    dog_grapes = AnimalFood.create(dog.id, grapes.id, "false")
    dog_garlic = AnimalFood.create(dog.id, garlic.id, "false")
    dog_xylitol = AnimalFood.create(dog.id, xylitol.id, "false")
    dog_nuts = AnimalFood.create(dog.id, nuts.id, "false")
    dog_butter = AnimalFood.create(dog.id, butter.id, "false")
    dog_nutmeg = AnimalFood.create(dog.id, nutmeg.id, "false")
    dog_onion = AnimalFood.create(dog.id, onion.id, "false")
    dog_liver = AnimalFood.create(dog.id, liver.id, "true")
    dog_citrus = AnimalFood.create(dog.id, citrus.id, "true")
    dog_corn = AnimalFood.create(dog.id, corn.id, "true")
    dog_peanuts = AnimalFood.create(dog.id, peanuts.id, "true")
    dog_apple_seeds = AnimalFood.create(dog.id, apple_seeds.id, "true")
    dog_bread = AnimalFood.create(dog.id, bread.id, "true")
    dog_banana = AnimalFood.create(dog.id, banana.id, "true")
    dog_watermelon =AnimalFood.create(dog.id, watermelon.id, "true")
    dog_carrot = AnimalFood.create(dog.id, carrot.id, "true")
    dog_salt = AnimalFood.create(dog.id, salt.id, "true")
    dog_dairy = AnimalFood.create(dog.id, dairy.id, "true")
    dog_non_toxic_mushrooms = AnimalFood.create(dog.id, non_toxic_mushrooms.id, "true")
    dog_pumpkin = AnimalFood.create(dog.id, pumpkin.id, "true")
    dog_broccoli = AnimalFood.create(dog.id, broccoli.id, "true")

    # dictionary = AnimalFood.all
    # print(dictionary)
    # id = 1
    # del dictionary[id]
    # print(dictionary)
    # print(AnimalFood.all)


seed_database()
