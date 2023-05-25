import random
from random import randint, choice
from enum import Enum


class Ability(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    BLOCK_DAMAGE_AND_REVERT = 4
    EXPLOSION = 5
    AGGRESSION = 6
    REVIVE = 7


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} | Health: {self.__health} | Damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.super_ability

    def hit(self, heroes):
        total_damage = self.damage
        for hero in heroes:
            if hero.health > 0:
                blocked_damage = min(total_damage, hero.health)
                hero.health -= blocked_damage
                total_damage -= blocked_damage
                if isinstance(hero, Berserk):
                    hero.blocked_damage += blocked_damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' | Defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coefficient = random.randint(2, 5)  # 2, 3, 4, 5
        if boss.health > 0:
            boss.health -= coefficient * self.damage
            print(f'Warrior hits critically {coefficient * self.damage}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BOOST)

    def apply_super_power(self, boss, heroes):
        pass


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, Ability.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        blocked_damage = random.randint(10, 30)
        self.blocked_damage += blocked_damage
        boss_damage = boss.damage - self.blocked_damage
        boss.health -= boss_damage
        print(f'Berserk blocks {self.blocked_damage} damage from the boss and deals {boss_damage} damage in return.')


def apply_super_power(self, boss, heroes):
    if boss.health > 0:
        boss.health -= self.damage
        print(f'Bomber explodes and deals {self.damage} additional damage to the boss.')


class Spitfire(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.AGGRESSION)

    def apply_super_power(self, boss, heroes):
        if boss.health > 0:
            print(f'Spitfire shows aggression and deals 80 additional damage to the boss.')
            boss.health -= 80


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.REVIVE)

    def apply_super_power(self, boss, heroes):
        first_dead_hero = next((hero for hero in heroes if hero.health <= 0), None)
        if first_dead_hero:
            print(f'Witcher revives {first_dead_hero.name} and sacrifices himself.')
            first_dead_hero.health = 1
            self.health = 0

class Bomber(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.EXPLOSION)

    def apply_super_power(self, boss, heroes):
        boss.health -= 100
        print(f'Bomber explodes and deals 100 additional damage to the boss.')

class Occultist(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.HEAL)

    def apply_super_power(self, boss, heroes):
        if self.health <= 0:
            return

        hero_to_heal = random.choice(heroes)
        if random.random() < 0.5:  # 50% шанс полностью исцелить героя
            if hasattr(hero_to_heal, 'max_health'):
                hero_to_heal.health = hero_to_heal.max_health
                print(f'Occultist fully heals {hero_to_heal.name}.')
        else:
            damage = self.damage
            if random.random() < 0.5:  # 50% что нанесет урон по герою
                hero_to_heal.health -= damage
                print(f'Occultist damages {hero_to_heal.name} for {damage} points.')

round_number = 0


def start():
    boss = Boss('Thor', 3500, 60) #Немно модифицыровал босса ато както не честно 9 пртоив 1го
    warrior = Warrior('Ahiles', 290, 10)
    doc = Medic('Aged Doc', 250, 5, 15)
    magic = Magic('Druid', 280, 15)
    berserk = Berserk('Max', 270, 10)
    assistant = Medic('Young', 300, 5, 5)
    bomber = Bomber('Bob', 250, 20)
    spitfire = Spitfire('John', 280, 12)
    witcher = Witcher('Geralt', 320, 8)
    occultist = Occultist('Occultist', 270, 8)
    heroes_list = [warrior, doc, magic, berserk, assistant, bomber, spitfire, witcher, occultist]

    show_stats(boss, heroes_list)
    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


def show_stats(boss, heroes):
    print(f'ROUND {round_number} --------------')
    print(boss)
    for hero in heroes:
        print(hero)

def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 \
                and boss.defence != hero.super_ability:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    show_stats(boss, heroes)

start()