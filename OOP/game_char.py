class Character:
    chars: list[dict] = []

    def __init__(self, name, health, level, ability: list[dict]):
        self.name = name
        self.__health = health
        self.level = level
        self.ability = ability
        Character.chars.append({'name': name, 'health': health, 'level': level, 'abil': ability})

    def level_up(self, level_up_by):
        self.level += level_up_by
        print(f"{self.name} is now at {self.level}")

    def add_new_ability(self, abil, pow_level):
        self.ability.append({abil: pow_level})
    
    @classmethod
    def display_chars(cls):
        levels_of_chars: list[dict] = []
        for char in cls.chars:
            levels_of_chars.append([char['name'], char['level']])

        print(sorted(levels_of_chars, key=lambda a: a[1]))

    def __add__(self, other: 'Character'):
        return Character(self.name + other.name, self.__health + other.__health,
                         self.level + other.level,
                         self.ability + other.ability)


class Wizard(Character):
    def __init__(self, name, health, level):
        super().__init__(name, health, level, [{'fly': 89}])
    

class Warrior(Character):
    def __init__(self, name, health, level):
        super().__init__(name, health, level, [{'fight': 100}])


    
char = Character('Jafar', 56, 2, [{'nothing': 100}])
another_char = Character('Name', 78, 6, [{'coding': 89}])


Character.display_chars()