# 7 užduotis
#	7.1 Apibrėžkite klasę ShoppingCart su atributu items (prekių kainų sąrašas, arba galite naudoti žodyną).
#	7.2 Pridėkite privatų metodą _calculate_discount, kuris taikys 10 % nuolaidą, jei bendra kaina viršija 100 Eur.
#	7.3 Pridėkite viešuosius metodus add_item, skirtus elementui pridėti į krepšelį, total_price, skirtus apskaičiuoti bendrą kainą, įskaitant visas nuolaidas, ir checkout, skirtus atspausdinti galutinę kainą pritaikius nuolaidą.
#	7.4 Sukurkite "ShoppingCart" objektą, pridėkite prekių ir išbandykite checkout metodą.

class ShoppingCart:
    items = {"obuolys": 1.25,
             "kriause":2.12,
             "pienas":2.49}
    
    def __init__(self) -> None:
        self.items = ShoppingCart.items
    
    def _calculate_discount(self, cart_items_price) -> float:
        if cart_items_price > 100:
            cart_items_price *= 0.9
        return round(cart_items_price, 2)
    
    def add_to_cart(self):
        cart_items = {}
        try:
            for key in self.items:
                cart_items.update({key: int(input(f"Kiek {key}?"))})
        except ValueError:
            print("Ivestis neteisinga, produktai nebus prideti")
        return cart_items
    
    def total_price(self):
        total_price = 0
        cart_items = self.add_to_cart()
        for key in cart_items:
            total_price += self.items[key] * cart_items[key]
        final_price = self._calculate_discount(total_price)
        return final_price

    def checkout(self):
        print(f"Galutine kaina, po nuolaidu {self.total_price()}")
    

krepselis = ShoppingCart()
krepselis.checkout()