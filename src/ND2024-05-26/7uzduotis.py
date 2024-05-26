#7 užduotis
#	7.1 Apibrėžkite klasę ShoppingCart su atributu _items (privatus žodynas, kurio raktai yra elementų pavadinimai, o reikšmės - kiekiai)
class ShoppingCart:
    def __init__(self, _items: dict) -> None:
        self._items = _items
#	7.2 Pridėkite privatų metodą _calculate_total, kuris grąžina bendrą krepšelio prekių skaičių.
    def _calculate_total(self):
        total_product_count = 0
        for item in self._items:
            total_product_count += self._items[item]
        return total_product_count
#	7.3 Pridėkite viešuosius metodus add_item, kad pridėtumėte prekę su nurodytu kiekiu, remove_item, kad pašalintumėte prekę, ir get_total_items, kad grąžintumėte bendrą krepšelio prekių skaičių.
    def add_item(self, item_to_add: dict):
        self._items.update(item_to_add)
    
    def remove_item(self, item_to_remove: dict):
        del self._items[item_to_remove]

    def get_total_items(self):
        print(self._calculate_total())
#	7.4 Užtikrinkite, kad metodai add_item ir remove_item atnaujintų krepšelį ir apskaičiuotų bendrą kiekį.

#	7.5 Sukurkite ShoppingCart objektą, pridėkite ir pašalinkite elementus ir gaukite bendrą elementų skaičių.
cart1 = ShoppingCart({"Obuolys": 5,
                      "Morka": 7,
                      "Kriause": 11})

cart1.get_total_items()
cart1.remove_item("Obuolys")
cart1.get_total_items()
cart1.add_item({"Obuolys": 8})
cart1.get_total_items()


