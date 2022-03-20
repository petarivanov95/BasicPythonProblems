#based on problem 8/chapter 3 from Tony Gaddis's Starting out with Python
import math

dog_pack = 10 # hot dogs per pack
bun_pack = 8 # bread buns for hot dog per pack

people_attending = int(input("How many people will attend? "))
dogs_person = int(input("How many hotdogs will each person eat? ")) #how many hot dogs will each person eat

dogs_required = dogs_person*people_attending

## math.ceil() Rounds a number upward to its nearest integer

dog_pack_to_buy = math.ceil(dogs_required/dog_pack) # gets the number of hot dog packs based on the num of people
bun_pack_to_buy = math.ceil(dogs_required/bun_pack) # gets the number of bread bun packs based on the num of people

print("There will be {} people attending the party.".format(people_attending))
print("Each of these people is planning to eat {} hot dogs.".format(dogs_person))
print("This means that we need to plan to have {} hot dogs prepared".format(dogs_required))
print("The organizer will need to buy {} packs of hot dogs and {} packs of buns.".format(dog_pack_to_buy,bun_pack_to_buy))
