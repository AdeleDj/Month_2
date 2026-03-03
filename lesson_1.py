# class Car:
#     # инициализатор (конструктор)
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#
# car1 = Car(color='black', model='Ford Mustang')
# car2 = Car(color='blue', model='Subaru Forester')
# print('Car 1:', car1.color, car1.model)
# print('Car2:', car2.color, car2.model)
# print(type(car1))


class Car:
    # инициализатор (конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model


car1 = Car(color='black', model='Ford Mustang')
car2 = Car(color='blue', model='Subaru Forester')
print('Car 1:', car1.color, car1.model)
print('Car2:', car2.color, car2.model)
print(type(car1))