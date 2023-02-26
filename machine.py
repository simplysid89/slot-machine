import random 

MAX_LINES = 3 #defining const value ie no of lines (1-3)
MAX_BET = 500  #defining const max and min value for betting 
MIN_BET = 10

ROWS= 3
COLS=3

symbols_count={
    'A':2,
    'B':4,
    'C':6,
    'D':8
}
#generate or run the slot machine using the values above
def get_slot_machine_spin(rows,cols,symbols):
    pass


#taking user inputs
def deposit():
    #keep asking the user for a valid 
    #amount until they dont give one
    while True:
        amount = input("Enter your amount = $")
        #check if amount is a number
        if amount.isdigit():
            #input() returns user input as string 
            #convert amount to int
            amount = int(amount)
            #check if amount > 0
            if amount>0:
                break
            else:
                print("amount must be greater than 0 ")
        else:
            print("enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("enter the number of lines to bet on between (1 -"+str(MAX_LINES)+")?")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("enter lines between (1-"+str(MAX_LINES)+")")
        else:
            print("enter a number")
    return lines        
def get_bet():
    while True:
        amount = input("enter the amount to bet on each line = $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("bet amount must be between ${}-${}".format(MIN_BET,MAX_BET))
        else:
            print("enter a number ")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total = bet*lines
        if total > balance:
            print(f"insuficient funds. Current balance is {balance}")
        else:
            break
    print("you are betting ${} on {} lines.Total bet is =${}".format(bet,lines,total))
   


main()

       
