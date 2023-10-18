#!/usr/bin/env python3
import sqlite3

from models.__init__ import CONN, CURSOR
from models.Animal import Animal
from models.Food import Food
from models.AnimalFood import AnimalFood

def seed_database():

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
    dog_food = Food.create("dog food")
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

    # dog
    dog_chocolate = AnimalFood.create(dog.id, chocolate.id, "false")
    dog_sweet_potatoes = AnimalFood.create(dog.id, sweet_potatoes.id, "true")
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

    # cat
    cat_chocolate = AnimalFood.create(cat.id, chocolate.id, "false")
    cat_sweet_potatoes = AnimalFood.create(cat.id, sweet_potatoes.id, "false")
    cat_dog_food = AnimalFood.create(cat.id, dog_food.id, "false")
    cat_avocado = AnimalFood.create(cat.id, avocado.id, "false")
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

    # bird
    bird_chocolate = AnimalFood.create(bird.id, chocolate.id, "false")
    bird_sweet_potatoes = AnimalFood.create(bird.id, sweet_potatoes.id, "true")
    bird_dog_food = AnimalFood.create(bird.id, dog_food.id, "true")
    bird_avocado = AnimalFood.create(bird.id, avocado.id, "false")
    bird_grapes = AnimalFood.create(bird.id, grapes.id, "false")
    bird_garlic = AnimalFood.create(bird.id, garlic.id, "false")
    bird_xylitol = AnimalFood.create(bird.id, xylitol.id, "false")
    bird_nuts = AnimalFood.create(bird.id, nuts.id, "false")
    bird_butter = AnimalFood.create(bird.id, butter.id, "false")
    bird_nutmeg = AnimalFood.create(bird.id, nutmeg.id, "false")
    bird_onion = AnimalFood.create(bird.id, onion.id, "false")
    bird_liver = AnimalFood.create(bird.id, liver.id, "false")
    bird_citrus = AnimalFood.create(bird.id, citrus.id, "true")
    bird_corn = AnimalFood.create(bird.id, corn.id, "false")
    bird_peanuts = AnimalFood.create(bird.id, peanuts.id, "false")
    bird_apple_seeds = AnimalFood.create(bird.id, apple_seeds.id, "false")
    bird_bread = AnimalFood.create(bird.id, bread.id, "false")
    bird_banana = AnimalFood.create(bird.id, banana.id, "true")
    bird_watermelon = AnimalFood.create(bird.id, watermelon.id, "true")
    bird_carrot = AnimalFood.create(bird.id, carrot.id, "true")
    bird_salt = AnimalFood.create(bird.id, salt.id, "false")
    bird_dairy = AnimalFood.create(bird.id, dairy.id, "false")
    bird_non_toxic_mushrooms = AnimalFood.create(bird.id, non_toxic_mushrooms.id, "true")
    bird_pumpkin = AnimalFood.create(bird.id, pumpkin.id, "true")
    bird_broccoli = AnimalFood.create(bird.id, broccoli.id, "true")    

seed_database()
