class Hero:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def action(self):
        print(f'{self.name} выполняет действие.')

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f'{self.name} был побежден.')
        else:
            print(f'{self.name} получил {damage} урона, здоровье теперь {self.health}.')