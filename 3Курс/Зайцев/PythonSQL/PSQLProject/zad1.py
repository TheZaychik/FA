"""
(4) 	Класс «Автобус».
Класс содержит свойства:
–	speed (скорость),
–capacity (максимальное количество пассажиров),
–	maxSpeed (максимальная скорость),
–	passengers (список имен пассажиров),
–	hasEmptySeats (наличие свободных мест),

–	seats (словарь мест в автобусе); методы:
–	посадка и высадка одного или нескольких пассажиров,  – увеличение и уменьшение скорости на заданное значение.
–	операции "in", "+=" и "−=" (посадка и высадка пассажира(ов) с заданной фамилией)

"""


class Bus:
    def __init__(self, speed: int, capacity: int, max_speed: int) -> None:
        self.speed = speed
        self.capacity = capacity
        self.max_speed = max_speed
        self.passengers = []
        self.has_empty_seats = capacity
        self.seats = {i: '' for i in range(self.capacity)}

    def add_passengers(self, passengers: list) -> None:
        if self.has_empty_seats >= len(passengers):
            self.passengers.extend(passengers)
            self.has_empty_seats -= len(passengers)
            for pas in passengers:
                for key in self.seats.keys():
                    if self.seats[key] == '':
                        self.seats[key] = pas
                        break
        else:
            print('Нельзя загрузить столько пассажиров')

    def remove_passengers(self, passengers: list) -> None:
        if self.capacity - self.has_empty_seats >= len(passengers):
            for pas in passengers:
                if pas in self.passengers:
                    self.passengers.pop(self.passengers.index(pas))
                    for key in self.seats.keys():
                        if self.seats[key] == pas:
                            self.seats[key] = ''
                            break
        else:
            print('Нельзя выгрузить столько пассажиров')

    def add_speed(self, speed: int) -> None:
        self.speed += speed

    def remove_speed(self, speed: int) -> None:
        self.speed -= speed

    def __iadd__(self, other: list) -> object:
        self.add_passengers(other)
        return self

    def __isub__(self, other: list) -> object:
        self.remove_passengers(other)
        return self

    def __contains__(self, item: str) -> object:
        return item in self.passengers


bus = Bus(60, 25, 120)
bus.add_passengers(['Ivan'])
print(bus.seats)
bus += ['Georgiy', 'Misha']
print(bus.seats)
bus -= ['Ivan']
print(bus.seats)
