from dataclasses import dataclass
from locales.skills import FuryPunch, HardShot, CriticalShot, Skill


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name='Воин',
    max_health=100,
    max_stamina=30,
    attack=0.8,
    armor=1.2,
    stamina=0.9,
    skill=FuryPunch(),
)  # TODO Инициализируем экземпляр класса UnitClass и присваиваем ему необходимые значения аттрибуотов

ThiefClass = UnitClass(
    name='Вор',
    max_health=60,
    max_stamina=50,
    attack=1.5,
    armor=1,
    stamina=1.2,
    skill=HardShot(),
)

ArcherClass = UnitClass(
    name='Лучник',
    max_health=45,
    max_stamina=70,
    attack=1.8,
    armor=1,
    stamina=1.5,
    skill=CriticalShot(),
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass,
    ArcherClass.name: ArcherClass
}
