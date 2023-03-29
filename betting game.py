import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1



ROWS = 3
COLS = 3

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)

    return winnings,winning_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(column) - 1:
               print(column[row],end = " | ")
            else:
                print(column[row])



def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("\nAmount must be greater than zero")
        else:
            print("\nPlease enter a number")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 -  "+str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= 3:
                break
            elif lines <= 0 and lines > 3:
                print("\nnumber of lines must be greater than zero and less than or equal to 3")
        else:
            print("\nPlease enter a number")
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if amount <= MAX_BET and amount >= MIN_BET:
                break
            else:
                print("\nAmount must be greater than zero and less than or equal to 100")
        else:
            print("\nPlease enter a number")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    bet = get_bet()
    Bet = bet * lines
    if Bet > balance:
        print(f"\nYou do not have enough to bet that amount. Your balance is {balance}")
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to = ${Bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_values)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines)
    return winnings - Bet
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")
main()