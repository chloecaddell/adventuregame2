from beginning import beginning

class Player():
    stamina = 5

    def __init__(self, character, username):
        self.character = character
        self.username = username

    def update_stamina(self, int):
        self.stamina += int

    def stamina_check(self):
        if self.stamina <= 0:
            print("You are tired, rest and return to your adventure later.")
            self.stamina = 5
            beginning(self)
        else:
            print(self.username, "Current Stamina:", self.stamina)