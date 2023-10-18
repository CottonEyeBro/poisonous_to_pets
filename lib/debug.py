#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb

# ipdb.set_trace()

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