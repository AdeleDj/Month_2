# родительский, суперкласс, parent class
class Car:
    # инициализатор(конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to(self, destination):
        print(f"Машина {self.model} едет в {destination}")

    def change_color(self, new_color):
        self.color = new_color


# дочерний класс, подкласс, child class
class Bus(Car):
    def drive_to(self, destination):
        super().drive_to(destination)
        print(f"Автобус {self.model} едет в {destination}")


class Truck(Car):
    def drive_to(self, destination):
        super().drive_to(destination)
        print(f"Грузовик {self.model} едет в {destination}")


bus_40 = Bus(color='green', model='Mercedes Benz')
print(bus_40.color, bus_40.model)
bus_40.drive_to("Bishkek")