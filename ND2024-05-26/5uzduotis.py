#5 užduotis
#	5.1 Apibrėžkite klasę Item su atributais name ir price.
class Item:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price

#	5.2 Apibrėžkite klasę Order su atributais order_id ir items (objektų Item sąrašas).
class Order:
    def __init__(self, order_id: str, items: list) -> None:
        self.order_id = order_id
        self.items = items

#	5.3 Pridėkite užsakymo metodus, kad galėtumėte pridėti elementą, pašalinti elementą ir apskaičiuoti bendrą kainą.
    def add_to_cart(self, item):
        self.items.append(item)

    def remove_from_cart(self, item):
        if item in self.items:
            self.items.remove(item)

    def checkout(self):
        sum = 0
        for item in self.items:
            sum += item.price
        print(f"Full price is {sum} eu")
#	5.4 Sukurkite Item ir Order objektus ir imituokite elementų pridėjimą/pašalinimą bei bendros kainos apskaičiavimą.
item1 = Item("Obuolys", 2)
item2 = Item("Morka", 1)
item3 = Item("Kefyras", 2.49)

order = Order("A000", [item1, item2])
print(order.checkout())
order.add_to_cart(item3)
print(order.checkout())
order.remove_from_cart(item1)
print(order.checkout())

