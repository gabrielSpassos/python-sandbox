#!/usr/bin/python
from datetime import datetime
from random import randint


class Person:
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking

    @classmethod
    def build_person_by_birthday_year(cls, name, birthday_year):
        age = cls.current_year - birthday_year
        return cls(name, age)

    def speak(self, subject):
        if self.eating:
            print(f'{self.name} is eating right now')
            return

        if self.speaking:
            print(f'{self.name} is already speaking')
            return

        print(f'{self.name} is speaking about {subject}')
        self.speaking = True

    def stop_speaking(self):
        if not self.speaking:
            print(f'{self.name} is not speaking')
            return

        print(f'{self.name} stop speaking')
        self.speaking = False

    def eat(self, food):
        if self.eating:
            print(f'{self.name} already ate')
            return

        print(f'{self.name} is eating {food}.')
        self.eating = True

    def stop_eating(self):
        if not self.eating:
            print(f'{self.name} is not eating')
            return

        print(f'{self.name} stop eating')
        self.eating = False

    def get_birthday_year(self):
        birth_day_year = self.current_year - self.age
        print(f'{self.name} was born at {birth_day_year}')
        return birth_day_year

    @staticmethod
    def create_id():
        id = randint(1000, 9999)
        print('ID:', id)
        return id
