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
    bird = Animal.create("bird")

    chocolate = Food.create("chocolate")
    sweet_potatoes = Food.create("sweet potatoes")
    grapes = Food.create("grapes")
    garlic = Food.create("garlic")
    xylitol = Food.create("xylitol")
    nuts = Food.create("nuts")
    butter = Food.create("butter")
    nutmeg = Food.create("nutmeg")
    salt = Food.create("salt")
    onion = Food.create("onion")
    liver = Food.create("liver")
    citrus = Food.create("citrus")
    corn = Food.create("corn")
    peanuts = Food.create("peanuts")
    apple_seeds = Food.create("apple seeds")
    bread = Food.create("bread")
    banana = Food.create("banana")
    watermelon = Food.create("watermelon")
    carrot = Food.create("carrot")
    dairy = Food.create("dairy")
    non_toxic_mushrooms = Food.create("non-toxic mushrooms")
    pumpkin = Food.create("pumpkin")
    broccoli = Food.create("broccoli")
    

    dog_chocolate = AnimalFood.create(dog.id, chocolate.id, "false")
    dog_sweet_potatoes = AnimalFood.create(dog.id, sweet_potatoes.id, "true")

    # cat cant consume corresponding comidas
    cat_chocolate = AnimalFood.create(cat.id, chocolate.id, "false")
    cat_sweet_potatoes = AnimalFood.create(cat.id, sweet_potatoes.id, "false")
    cat_avocado = AnimalFood.create(cat.id, cat_avocado.id, "false")
    cat_chocolate = AnimalFood.create(cat.id, cat_chocolate.id, "false")
    cat_grapes = AnimalFood.create(cat.id, cat_grapes.id, "false")
    cat_garlic = AnimalFood.create(cat.id, cat_garlic.id, "false")
    cat_xylitol = AnimalFood.create(cat.id, cat_xylitol.id, "false")
    cat_nuts = AnimalFood.create(cat.id, cat_nuts.id, "false")
    cat_butter = AnimalFood.create(cat.id, cat_butter.id, "false")
    cat_nutmeg = AnimalFood.create(cat.id, cat_nutmeg.id, "false")
    cat_onion = AnimalFood.create(cat.id, cat_onion.id, "false")
    cat_citrus = AnimalFood.create(cat.id, cat_citrus.id, "false")
    cat_corn = AnimalFood.create(cat.id, cat_corn.id, "false")
    cat_peanuts = AnimalFood.create(cat.id, cat_peanuts.id, "false")
    cat_apple_seeds = AnimalFood.create(cat.id, cat_apple_seeds.id, "false")
    cat_bread = AnimalFood.create(cat.id, cat_bread.id, "false")
    cat_watermelon = AnimalFood.create(cat.id, cat_watermelon.id, "false")
    cat_carrot = AnimalFood.create(cat.id, cat_carrot.id, "false")
    cat_salt = AnimalFood.create(cat.id, cat_salt.id, "true")
    cat_dairy = AnimalFood.create(cat.id, cat_dairy.id, "false")
    cat_non_toxic_mushrooms = AnimalFood.create(cat.id, cat_non_toxic_mushrooms.id, "true")
    cat_pumpkin = AnimalFood.create(cat.id, cat_pumpkin.id, "true")
    cat_broccoli = AnimalFood.create(cat.id, cat_broccoli.id, "true")





    # dictionary = AnimalFood.all
    # print(dictionary)
    # id = 1
    # del dictionary[id]
    # print(dictionary)
    # print(AnimalFood.all)


seed_database()