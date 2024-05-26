#6 užduotis
#	6.1 Apibrėžkite klasę FitnessTracker su atributais user_name ir _steps (private).
class FitnessTracker:
    def __init__(self, user_name: str, _steps = 0) -> None:
        self.user_name = user_name
        self._steps = _steps
#	6.2 Pridėkite privatų metodą _check_goal, kuris spausdina pranešimą, jei pasiekiamas tam tikras žingsnių tikslas (pvz., 10 000 žingsnių).
    def _check_goal(self, goal = 10000):
        if self._steps >= goal:
            print("Goal achieved")
        else:
            pass
#	6.3 Pridėkite viešuosius metodus add_steps, skirtus žingsniams pridėti, reset_steps, skirtus žingsnių skaičiui atstatyti, ir get_steps, skirtus dabartiniam žingsnių skaičiui grąžinti.
    def add_steps(self, steps_to_add):
        self._steps += steps_to_add
        self._check_goal()
    
    def reset_steps(self, steps_to_add):
        self._steps = 0

    def get_steps(self):
        return self.get_steps
#	6.4 Užtikrinkite, kad add_steps metodas po žingsnių atnaujinimo iškviestų _check_goal.
#	6.5 Sukurkite FitnessTracker objektą ir pritaikykite metodus.

tracker1 = FitnessTracker("Matas")
tracker1.add_steps(5000)
print("smh")
tracker1.add_steps(5000)

