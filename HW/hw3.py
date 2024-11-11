# Система бронирования номеров в отеле

from abc import ABC, abstractmethod

class Room (ABC):
    def __init__(self, features, price):
        self._features = features
        self._price = price


    @abstractmethod
    def get_price(self):
        """Возвращает цену номера"""
        pass

    @abstractmethod
    def get_features(self):
        """Возвращает список удобств в номере"""
        pass

class StandardRoom(Room):
    def get_price(self):
        return self._price

    def get_features(self):
        return self._features


class LuxuryRoom(Room):
    def get_price(self):
        return self._price

    def get_features(self):
        return self._features


class FamilyRoom(Room):
    def get_price(self):
        return self._price

    def get_features(self):
        return self._features

class WiFiService:
    def get_wifi_description(self):
        return "Высокоскоростный файвай доступен"

class BreakfastService:
    def get_breakfast_description(self):
        return "Завтрак включен"

class LuxuryRoom(Room, WiFiService, BreakfastService):
    def get_price(self):
        return self._price

    def get_features(self):
        return self._features + [self.get_wifi_description(), self.get_breakfast_description()]


class FamilyRoom(Room, WiFiService):
    def get_price(self):
        return self._price

    def get_features(self):
        return self._features + [self.get_wifi_description()]

standard_room = StandardRoom(features=["телевизор", "маленький холодильник"], price=100)
luxury_room = LuxuryRoom(features=["телевизор", "маленький холодильник", "балкон"], price=200)
family_room = FamilyRoom(features=["телевизор", "маленький холодильник", "дополнительные кровати"], price=150)

print("Standard Room:")
print("Price:", standard_room.get_price())
print("Features:", standard_room.get_features())

print("\nLuxury Room:")
print("Price:", luxury_room.get_price())
print("Features:", luxury_room.get_features())

print("\nFamily Room:")
print("Price:", family_room.get_price())
print("Features:", family_room.get_features())