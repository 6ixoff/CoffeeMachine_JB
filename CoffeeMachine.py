class CoffeeMachine:
    def __init__(self):
        self.water_remainder = 400
        self.milk_remainder = 540
        self.beans_remainder = 120
        self.balance = 550
        self.disposable_cups = 9
        self.state = None

    def check_remainder(self, water_require, milk_require, beans_require, cups_require ):
        check_results = [(self.water_remainder - water_require) >= 0, (self.milk_remainder - milk_require) >= 0, (self.beans_remainder - beans_require) >= 0, (self.disposable_cups - cups_require) >= 0]
        if all(check_results):
            ability = 0
            if milk_require == 0:
                ability = min(self.water_remainder // water_require, self.beans_remainder // beans_require, self.disposable_cups // cups_require)
            else:
                ability = min(self.water_remainder // water_require, self.milk_remainder // milk_require, self.beans_remainder // beans_require, self.disposable_cups // cups_require)
            if ability == 1:
                print("Yes, I can make that amount of coffee ")
                return True
            elif ability > 1:
                print(f"Yes, I can make that amount of coffee (and even {ability - 1} more than that)")
                return True
            else:
                print(f"No, I can make only {ability} cups of coffee")
        else:
            names = ["water", "milk", "coffee beans", "disposable cups"]
            not_enough = ""
            for i in range(4):
                if not check_results[i]:
                    if len(not_enough) > 0:
                        not_enough += (", " + names[i])
                    else:
                        not_enough += names[i]
            print(f"Sorry, not enough {not_enough}!")
            return False

    def show_the_remainder(self):
        print('The coffee machine has: ')
        print(f'{self.water_remainder} of water')
        print(f'{self.milk_remainder} of milk')
        print(f'{self.beans_remainder} of coffee beans')
        print(f'{self.disposable_cups} of disposable cups')
        print(f'{self.balance} of money')

    def buy(self, product):
        if product == '1':
            if self.check_remainder(250, 0, 16, 1):
                self.water_remainder -= 250
                self.beans_remainder -= 16
                self.disposable_cups -= 1
                self.balance += 4
                return True
            else:
                return True
        elif product == '2':
            if self.check_remainder(350, 75, 20, 1):
                self.water_remainder -= 350
                self.milk_remainder -= 75
                self.beans_remainder -= 20
                self.disposable_cups -= 1
                self.balance += 7
                return True
            else:
                return True
        elif product == '3':
            if self.check_remainder(200, 100, 12, 1):
                self.water_remainder -= 200
                self.milk_remainder -= 100
                self.beans_remainder -= 12
                self.disposable_cups -= 1
                self.balance += 6
                return True
            else:
                return True
        elif product == "back":
            return True
        else:
            print("Enter correct product, please")
            return False

    def fill(self, water_increase, milk_increase, beans_increase, cups_increase):
        self.water_remainder += water_increase
        self.milk_remainder += milk_increase
        self.beans_remainder += beans_increase
        self.disposable_cups += cups_increase

    def take(self):
        print(f'I gave you ${self.balance}')
        self.balance -= self.balance

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

if __name__ == '__main__':
    coffee_machine = CoffeeMachine()
    while True:
        if coffee_machine.get_state() == None:
            action = input("Write action (buy, fill, take, remaining, exit): ")
            coffee_machine.set_state(action)
        else:
            if coffee_machine.get_state() == "buy":
                while True:
                    product = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
                    if coffee_machine.buy(product):
                        coffee_machine.set_state(None)
                        break
            elif coffee_machine.get_state() == "fill":
                water_increase = int(input('Write how many ml of water do you want to add: '))
                milk_increase = int(input('Write how many ml of milk do you want to add: '))
                beans_increase = int(input('Write how many grams of coffee beans do you want to add: '))
                cups_increase = int(input('Write how many disposable cups of coffee do you want to add: '))
                coffee_machine.fill(water_increase, milk_increase, beans_increase, cups_increase)
                coffee_machine.set_state(None)
            elif coffee_machine.get_state() == "take":
                coffee_machine.take()
                coffee_machine.set_state(None)
            elif coffee_machine.get_state() == "remaining":
                coffee_machine.show_the_remainder()
                coffee_machine.set_state(None)
            elif coffee_machine.get_state() == "exit":
                break
            else:
                print("Write action one else")
                coffee_machine.set_state(None)
