# задание 1

class Bike:
    def __init__(self, color, price):
        self.color = color
        self.price = price


testOne = Bike("синий", 89.99)
testTwo = Bike("фиолетовый", 25.0)

# проверка задания 1
print("Задание 1\n")
print("Первый велосипед:")
print(f"Цвет: {testOne.color}, Цена: {testOne.price}\n")

print("Второй велосипед:")
print(f"Цвет: {testTwo.color}, Цена: {testTwo.price}\n")

# задание 2

class AppleBasket:
    def __init__(self, color, quantity):

        self.apple_color = color
        self.apple_quantity = quantity

    def increase(self):
        # увеличение количества яблок на 1
        self.apple_quantity += 1

    def __str__(self):
        return f"Корзина яблок с {self.apple_quantity} яблоками, цвет: {self.apple_color}."

# проверка задания 2
print("Задание 2\n")
my_basket = AppleBasket("красный", 4)
print(my_basket) 

my_basket.increase() # + 1
my_basket.increase() # + 1
print(my_basket)

# задание 3

class BankAccount:
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def __str__(self):
        return f"На вашем счете, {self.name}, есть доллары {self.amt}"

# проверка задания 3
print("\nЗадание 3\n")

t1 = BankAccount("Bob", 100)
print(t1)