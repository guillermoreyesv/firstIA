from ia import FirstIA


class Root:
    def __init__(self):
        inches_list = [1, 3, 5, 100, 105, 107]
        IA = FirstIA(inches=inches_list)
        IA.train(epochs=10000, verbose=False)
        self.IA = IA
        self.inches = 0

    def main(self):
        self.give_me_inches()
        self.calculate()
        self.another_try()

    def give_me_inches(self):
        try:
            print('How many inches do you want to convert to centimeters')
            self.inches = float(input())
        except Exception:
            print('Only numbers (int/float)')
            self.give_me_inches()

    def calculate(self):
        result = self.IA.predict(self.inches)
        print(f'{self.inches} IN > {result} CM')

    def another_try(self):
        print('Do you wanna another convertion? (YES/NO)')
        response = str(input()).lower().strip()
        if response in ['yes', 'y', 'si', 's']:
            self.main()