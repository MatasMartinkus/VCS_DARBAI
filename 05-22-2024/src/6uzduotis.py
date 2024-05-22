#6 užduotis
#	6.1 Apibrėžkite klasę PasswordValidator su atributu password.
#	6.2 Pridėkite privačius metodus _has_uppercase, _has_lowercase ir _has_digit kurie grąžina True, jei slaptažodyje yra bent viena didžioji raidė, mažoji raidė ar skaitmuo.
#	6.3 Pridėkite viešąjį (public) metodą is_valid, kuris, naudodamasis šiais privačiaisiais metodais, tikrina, ar slaptažodis yra galiojantis.
#	6.4 Sukurkite PasswordValidator objektą ir išbandykite metodą is_valid.

class PasswordValidator:
    def __init__(self, password:str) -> None:
        self.password = password

    def _has_uppercase(self) -> bool:
        for char in self.password:
            if char.isupper():
                return True
    
    def _has_lowercase(self) -> bool:
        for char in self.password:
            if char.islower():
                return True
            
    def _has_digit(self) -> bool:
        for char in self.password:
            if char.isdigit():
                return True
            
    def is_valid(self) -> bool:
        if self._has_digit() and self._has_lowercase() and self._has_uppercase():
            return True
        else:
            return False
        
password1 = PasswordValidator("Slap")

print(password1.is_valid())