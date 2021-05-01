"""
Создать класс воина, создать 2 или больше объектов воина с соответствующими воину атрибутами. Реализовать методы,
которые позволять добавить здоровья, сменить оружие. Реализовать возможность драки 2х воинов с потерей здоровья,
приобретения опыта.
Следует учесть:
 - у воина может быть броня
 - здоровье не может быть меньше 0
 - броня не может быть меньше 0
 - здоровье не тратится пока броня не 0
Было бы неплохо добавить возможность воину носить несколько видов оружия и при сломаном текущем заменить его (опционально)
"""
from random import randint, choice
from typing import NamedTuple


class Weapon(NamedTuple):
    name: str
    power: int

counter = 1


class Warrior:
    def __init__(self, weapon: Weapon, name: str, health: int):
        self.weapon = weapon
        self.name = name
        self.health = health
        self.armor = randint(1, 50)
        self.status = 'alive'

    def add_health(self):
        self.health += randint(10, 50)
        if self.health > 101:
            self.health = 101

    def change_weapon(self):
        self.weapon = random_choose_weapon()

    def add_armor(self):
        self.armor = randint(10, 50)

    def heat_other(self, other_warrior):
        summ = other_warrior.health + other_warrior.armor - self.weapon.power
        global counter
        counter += 0.5
        if summ <= 0:
            other_warrior.status = 'die'
        if other_warrior.status == 'die':
            print(other_warrior.name + ' is die')
            raise Exception
        if 101 >= summ > 0:
            other_warrior.health = summ
        if summ > 101:
            other_warrior.health = 101


def random_choose_weapon():
    weapon_list = []
    for i in range(50):
        weapon_list.append(Weapon(
            name=str(i),
            power=randint(1, 101)
        ))
    return choice(weapon_list)


def main_fighting_area():
    samuray = Warrior(name='Oleg', health=100, weapon=random_choose_weapon())
    viking = Warrior(name='Olof', health=100, weapon=random_choose_weapon())
    while True:
        print('------ Round №', int(counter), '------')
        print(samuray.weapon.power, 'samuray weapon power')
        print(samuray.health, 'samuray health')
        print(samuray.armor, 'samuray armor')
        print(viking.weapon.power, 'viking weapon power')
        print(viking.health, 'viking health')
        print(viking.armor, 'viking armor')
        samuray.heat_other(viking)
        print('after')
        print(viking.health, 'viking health')
        viking.heat_other(samuray)
        print('after')
        print(samuray.health, 'samuray health')
        samuray.add_health()
        viking.add_health()
        samuray.add_armor()
        viking.add_armor()
        samuray.change_weapon()
        viking.change_weapon()

main_fighting_area()

