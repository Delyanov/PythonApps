class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        o = super().__new__(cls)
        cls.houses_history.append(args[0])
        return o

    def __del__(self):
        print(self.name, " снесён, но он останется в истории")

    def __init__(self, name, number):
        #имя
        self.name = name
        #кол-во этажей
        self.number_of_floors = number

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return "Название: "+ self.name + ", кол-во этажей: " + str(self.number_of_floors)

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            self.number_of_floors+=value
        elif isinstance(self, int):
            value.number_of_floors +=self
            return value
        elif isinstance(value, House):
            self.number_of_floors+=value.number_of_floors
        return self

    def go_to(self, new_floor):
        if new_floor<1 or new_floor>self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for n in range(int(new_floor)):
                print(n+1)

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

del h1
