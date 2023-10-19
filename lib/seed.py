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
    avocado = Food.create("avocado")
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
    cat_sweet_potatoes = AnimalFood.create(cat.id, sweet_potatoes.id, "true")
    cat_avocado = AnimalFood.create(cat.id, avocado.id, "false")
    cat_chocolate = AnimalFood.create(cat.id, chocolate.id, "false")
    cat_grapes = AnimalFood.create(cat.id, grapes.id, "false")
    cat_garlic = AnimalFood.create(cat.id, garlic.id, "false")
    cat_xylitol = AnimalFood.create(cat.id, xylitol.id, "false")
    cat_nuts = AnimalFood.create(cat.id, nuts.id, "false")
    cat_butter = AnimalFood.create(cat.id, butter.id, "false")
    cat_nutmeg = AnimalFood.create(cat.id, nutmeg.id, "false")
    cat_onion = AnimalFood.create(cat.id, onion.id, "false")
    cat_citrus = AnimalFood.create(cat.id, citrus.id, "false")
    cat_corn = AnimalFood.create(cat.id, corn.id, "true")
    cat_peanuts = AnimalFood.create(cat.id, peanuts.id, "true")
    cat_apple_seeds = AnimalFood.create(cat.id, apple_seeds.id, "true")
    cat_bread = AnimalFood.create(cat.id, bread.id, "true")
    cat_banana = AnimalFood.create(cat.id, banana.id, "true")
    cat_watermelon = AnimalFood.create(cat.id, watermelon.id, "true")
    cat_carrot = AnimalFood.create(cat.id, carrot.id, "true")
    cat_salt = AnimalFood.create(cat.id, salt.id, "true")
    cat_dairy = AnimalFood.create(cat.id, dairy.id, "false")
    cat_non_toxic_mushrooms = AnimalFood.create(cat.id, non_toxic_mushrooms.id, "true")
    cat_pumpkin = AnimalFood.create(cat.id, pumpkin.id, "true")
    cat_broccoli = AnimalFood.create(cat.id, broccoli.id, "true")





    # dictionary = AnimalFood.all
    # print(dictionary)
    # id = 1
    # del dictionary[id]
    # print(dictionary)
    # print(AnimalFood.all)


seed_database()