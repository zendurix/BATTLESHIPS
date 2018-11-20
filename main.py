from classes import Place
import os
from random import randint
import time


def clear():
    os.system('cls')


def print_field(field):
    print('')
    x = 0
    for i in field:
        for j in field[x]:
            print(j.pformat, end=' ')
        print('')
        x += 1


def user_place_ship(field):
    good_target = False
    while not good_target:
        ch_x = int(input())
        ch_y = int(input())
        a = 0
        for i in field:
            for j in field[a]:
                if j.x == ch_x and j.y == ch_y:
                    if j.state == 'ship':
                        print("there is ship, type another cord")
                        continue
                    j.place_ship()
                    good_target = True
                    continue
            a += 1


def random_place_ship(field):
    good_target = False
    while not good_target:
        ch_x = randint(0, 4)
        ch_y = randint(0, 4)
        a = 0
        for i in field:
            for j in field[a]:
                if j.x == ch_x and j.y == ch_y:
                    if j.state == 'ship':
                        print("there is ship, type another cord")
                        continue
                    j.bot_place_ship()
                    good_target = True
                    continue
            a += 1


def shooting(field):
    good_target = False
    while not good_target:
        ch_x = int(input())
        ch_y = int(input())
        a = 0
        for i in field:
            for j in field[a]:
                if j.x == ch_x and j.y == ch_y:
                    if (j.state != 'wreck') and j.state != 'miss':
                        j.shot()
                        good_target = True
                        continue
                    else:
                        print("target is arleady shooted, type another ")
                        continue
            a += 1


def bot_shooting(field):
    good_target = False
    while not good_target:
        ch_x = randint(0, 4)
        ch_y = randint(0, 4)
        a = 0
        for i in field:
            for j in field[a]:
                if j.x == ch_x and j.y == ch_y:
                    if (j.state != 'wreck') and j.state != 'miss':
                        j.bot_shot()
                        good_target = True
                        continue
                    else:
                        print("target is arleady shooted, type another ")
                        continue
            a += 1


w, h = 5, 5
field_usr = [[Place(Place.x, Place.y, Place.id_counter) for x in range(w)] for y in range(h)]

Place.x = 0
Place.y = 0

field_bot = [[Place(Place.x, Place.y, Place.id_counter) for x in range(w)] for y in range(h)]

ship_count = 4
print("BATTLE SHIPS V0.0")
print("0 - empty space \nS - ship \nx - missed shot \n W - wreck")
input("type anything to proceed")

for i in range(4):
    print_field(field_usr)
    print("place your ships \nships left: ", ship_count, "\ntype [x value] + [enter] + [y value] + [enter] ")
    print("x and y are in range <0,4>")
    user_place_ship(field_usr)
    ship_count -= 1
    clear()
input("type anything to proceed to bot ships placement")
for i in range(4):
    clear()
    print("bot is placing his ships ")
    random_place_ship(field_bot)

time.sleep(1)

while (Place.usr_ship_count != 0) and (Place.bot_ship_count != 0):
    clear()
    print("Your board: ")
    print_field(field_usr)
    print("\n\n")

    print("Bot board: ")
    print_field(field_bot)

    print("\ntype x and y to shoot at your enemy territory: ")
    shooting(field_bot)

    print("\n bot is shooting: ")
    bot_shooting(field_usr)
    time.sleep(1)


if Place.usr_ship_count == 0:
    print("looser!!!")
if Place.bot_ship_count == 0:
    print("Winner!!!")

input("type anything to proceed")
time.sleep(5)
