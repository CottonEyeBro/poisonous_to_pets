import sqlite3

CONN = sqlite3.connect('safety.db')
CURSOR = CONN.cursor()