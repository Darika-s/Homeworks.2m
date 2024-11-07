from main import Hero

class MyHero(Hero):
    def __init__(self, name, health, power, skill_power):
        super().__init__(name, health, power)
        self.skill_power = skill_power
    def special_skill(self):
        if self.skill_power > 0:
            print(f'{self.name} использует особое умение')
            self.skill_power -= 1
        else:
            print(f'{self.name} не осталось сил для использования умения.')

    def action(self):
        super().action()
        self.special_skill()

if __name__ == '__main__':
    hero = MyHero(name='SuperHero', health=100, power=50, skill_power=5)
    hero.action()
    print(f'Текущее здоровье: {hero.health}')
    print(f'Оставшаяся сила способности: {hero.skill_power}')

