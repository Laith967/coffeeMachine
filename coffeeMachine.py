import sys

class CoffeeMachine:
    water = int(400)
    milk = int(540)
    coffee = int(120)
    cups = int(9)
    money = int(550)

    espresso = [-250, 0, -16, -1, 4]
    latte = [-350, -75, -20, -1, 7]
    cappuccino = [-200, -100, -12, -1, 6]

    user_input = None
    state = "default"

    def check_action(self):
        while True:
            action = input('\nWrite action (buy, fill, take, remaining, exit):\n')
            if action == "buy":
                self.coffee_variants()
            elif action == "fill":
                self.fill_ingredients()
            elif action == "take":
                print(f"I gave you ${self.money}")
                self.money = 0
            elif action == "remaining":
                self.display_info()
            elif action == "exit":
                sys.exit()

    def coffee_variants(self):
        variant = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
        if variant == '1':
            self.check_ingredients(self.espresso)
        elif variant == '2':
            self.check_ingredients(self.latte)
        elif variant == '3':
            self.check_ingredients(self.cappuccino)
        elif variant == "back":
            self.check_action()

    def ingredients(self, get_resource):
        self.water += get_resource[0]
        self.milk += get_resource[1]
        self.coffee += get_resource[2]
        self.cups += get_resource[3]
        self.money += get_resource[4]

    def fill_ingredients(self):
        options = []
        options.append(int(input('\nWrite how many ml of water do you want to add:\n')))
        options.append(int(input('Write how many ml of milk do you want to add:\n')))
        options.append(int(input('Write how many grams of coffee beans do you want to add:\n')))
        options.append(int(input('Write how many disposable cups of coffee do you want to add:\n')))
        options.append(int(0))
        self.ingredients(options)

    def check_ingredients(self, get_resource):
        str1 = ["water,", "milk,", "coffee beans,", "disposable cups,"]
        if -get_resource[0] <= self.water and -get_resource[1] <= self.milk and -get_resource[2] <= self.coffee\
                and -get_resource[3] < self.cups:
            print("I have enough resources, making you a coffee!")
            self.ingredients(get_resource)
        else:
            if -get_resource[0] < self.water:
                str1.remove("water,")
            if -get_resource[1] < self.milk:
                str1.remove("milk,")
            if -get_resource[2] < self.coffee:
                str1.remove("coffee beans,")
            if -get_resource[3] < self.cups:
                str1.remove("disposable cups,")
            str2 = 'Sorry, not enough ' + " ".join(str1)
            str2 = str2[0:-1] + '!'
            print(str2)

    def display_info(self):
        print(f'\nThe coffee machine has:\n'
              f'{self.water} of water\n'
              f'{self.milk} of milk\n'
              f'{self.coffee} of coffee beans\n'
              f'{self.cups} of disposable cups\n'
              f'${self.money} of money')

go = CoffeeMachine()
go.check_action()