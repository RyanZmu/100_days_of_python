from prettytable import PrettyTable

class MoneyMachine:
    def __init__(self) -> None:
        self.coin_values = {
            'quarters': .25,
            'dimes': .10,
            'nickels': .05
        }

    def transaction(self,coffee_bought,payment):
        # Get total expected payment
        payment_made = False
        change_due = 0

        table = PrettyTable()

        # Split coin values
        payment = payment.split(",")

        # Format coins given
        formated_payment = []
        for coins in payment:
            formated_payment.append(coins)

        total_money_given = int(formated_payment[0]) * self.coin_values['quarters'] + int(formated_payment[1]) * self.coin_values['dimes'] + int(formated_payment[2]) * self.coin_values['nickels']

        # check if enough money was given
        if total_money_given < coffee_bought.cost:
            payment_made = False
            print(f"Error! Not enough money! Need ${coffee_bought.cost - total_money_given} more! Retry transaction...")
            add_more_money = input("Would you like to add more? Y/N")

            # Add more money if short
            if add_more_money.lower() == 'y':
                deposit_amount = float(input("Enter amount to add in decimals ($1.25 = 1.25) \n"))
                total_money_given += deposit_amount
            else:
                print('Restarting transaction...')
                return

        # If more than needed, give change
        if total_money_given > coffee_bought.cost:
            payment_made = True

            # Process Change
            change_due = round(total_money_given - coffee_bought.cost, 2)

        # If exact, process transaction
        if total_money_given == coffee_bought.cost:
            payment_made = True

        # Create reciept when payment is made
        if payment_made:
            table.field_names = ["Item","Total","Paid","Change Due"]
            table.add_row([coffee_bought.name,f'${coffee_bought.cost}',f'${total_money_given}',f'${change_due}'])
            print(table)
        return payment_made
