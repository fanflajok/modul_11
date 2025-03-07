import inspect
from pprint import pprint


class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __init__(self, appart_comp_name, number_of_floors):
        self.appart_comp_name = appart_comp_name
        self.number_of_floors = int(number_of_floors)
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"There's no floor № {new_floor} in {self.appart_comp_name}")
        else:
            for i in range(new_floor):
                print(i+1)
            print(f"You have arrived on the {i+1} floor in the {self.appart_comp_name}")
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f"There are {self.number_of_floors} floors in the {self.appart_comp_name}")
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            print(f"Numbers of floors in {self.appart_comp_name} was increased by {value}")
        return self
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)
h1 = House("Luigi's Mansion", 16)
h2 = House("Princess Peach's Castle", 3)
h3 = House("Toad's Home", 2)
h4 = House("Twinsan's House", 3)




def  introspection_info(obj):
    return type(obj),obj.__dict__, dir(obj),inspect.getmodule(obj)
pprint(introspection_info(h1))

