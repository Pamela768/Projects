"""This code creates a password using the users name and year of birth"""

import random
import time

name= ""
year = ""

name = input("Hey yoooo!!! What is your name ")


year = str(input("That's a preety cool name, Now What year wear you born?"))


print("Can you guess what I'm gonna do ")
time.sleep(2)
print("I'm gonna create a super cool password uot of yor name. Noww....\n Just give me a second")

first = random.choice(name)
second = random.choice(year)
third = random.choice(name)
fourth =  random.choice(year)
fifth =  random.choice(name)
sixth =  random.choice(year)

Password = first+second+third+fourth+fifth+sixth

print (f"There we are \n Your password is {Password}.")
