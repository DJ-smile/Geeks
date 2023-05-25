class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    # setters
    def set_cpu(self, cpu):
        self.__cpu = cpu

    def set_memory(self, memory):
        self.__memory = memory

    # getters
    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory

    def make_computations(self):
        result = 0
        try:
            result = int(self.__cpu) + int(self.__memory)
        except ValueError:
            return "Error: can't perform calculations with non-numeric values"
        return result

    # magic methods
    def __str__(self):
        return f"Computer: CPU - {self.__cpu}, Memory - {self.__memory}"

    def __eq__(self, other):
        if isinstance(other, Computer):
            return self.__memory == other.get_memory()
        return False

    def __ne__(self, other):
        if isinstance(other, Computer):
            return self.__memory != other.get_memory()
        return True

    def __lt__(self, other):
        if isinstance(other, Computer):
            return self.__memory < other.get_memory()
        return False

    def __gt__(self, other):
        if isinstance(other, Computer):
            return self.__memory > other.get_memory()
        return False

    def __le__(self, other):
        if isinstance(other, Computer):
            return self.__memory <= other.get_memory()
        return False

    def __ge__(self, other):
        if isinstance(other, Computer):
            return self.__memory >= other.get_memory()
        return False


class Phone:
    def __init__(self):
        self.__sim_cards_list = []

    # setters
    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # getters
    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def call(self, sim_card_number, call_to_number):
        if sim_card_number < 1 or sim_card_number > len(self.__sim_cards_list):
            print("Error: invalid sim card number")
        else:
            operator = self.__sim_cards_list[sim_card_number - 1]
            print(f"Calling {call_to_number} from {operator} operator")

    # magic method
    def __str__(self):
        return f"Phone: sim cards - {self.__sim_cards_list}"


def use_gps(location):
    print(f"Creating a route to {location} using GPS")


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self)
        self.__sim_cards_list = sim_cards_list

    # magic method
    def __str__(self):
        return f"SmartPhone: CPU - {self.get_cpu()}, " \
               f"Memory - {self.get_memory()}, sim cards - {self.get_sim_cards_list( )}"


# creating objects
comp = Computer("Intel Core i7", "16GB")
phone = Phone()
smartphone1 = SmartPhone("Intel Core i5", "8GB", ["Beeline", "Megacom"])
smartphone2 = SmartPhone("AMD Ryzen 5", "8GB", ["O!", "Beeline"])

# testing methods
print(comp.make_computations())
phone.set_sim_cards_list(["Beeline", "Megacom", "O!"])
phone.call(1, "+996 777 99 88 11")
use_gps("Bishkek")
use_gps("Almaty")

# printing object information
print(comp)
print(phone)
print(smartphone1)
print(smartphone2)

# testing comparison operators for Computer class
print(comp == smartphone1)  # compares memory attribute of comp and smartphone1
print(smartphone1 != smartphone2)  # compares memory attribute of smartphone1 and smartphone2
print(smartphone1 > smartphone2)  # compares memory attribute of smartphone1 and smartphone2
print(smartphone1 >= smartphone2)  # compares memory attribute of smartphone1 and smartphone2
print(smartphone1 < smartphone2)  # compares memory attribute of smartphone1 and smartphone2
print(smartphone1 <= smartphone2)  # compares memory attribute of smartphone1 and smartphone2
