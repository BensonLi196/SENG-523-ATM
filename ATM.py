import tkinter as tk
from tkinter import messagebox
from tkinter import *


ATM_Home = tk.Tk() # Main window
ATM_Home.geometry("500x500")

CardInserted = False #Is there a card inserted or not
InsertedCard = None #The card number of the currently inserted card
max_allowable_withdraw = 1000 #Maximum allowed for one withdrawal
CurrentAccount = ["", "", False, 0]

#The amount of bills in the ATM
five_dollar_bills = 0
ten_dollar_bills = 100
twenty_dollar_bills = 100
fifty_dollar_bills = 100
hundred_dollar_bills = 0

Total = (five_dollar_bills * 5) + (ten_dollar_bills * 10) + (twenty_dollar_bills * 20) + (fifty_dollar_bills & 50) + (hundred_dollar_bills * 100)  #Total amount of money in the ATM

#Pre-loaded accounts. Format: [Card Number, Pin, Status, Balance]
cards = [["123456", "523", True, 5000.00], ["789101112", "550", True, 1000.00], ["1314151617", "511", False, 850.99]] #List of all card numbers
card_nums = ["123456","789101112","1314151617"]

def check_status(card_num):
    i = 0
    while i < len(cards):
        if card_num == cards[i][0]:
            if True in cards[i]:
                return True
            else:
                return False
        i+=1


def check_pin(card_num, PIN):
    i = 0
    while i < len(cards):
        if card_num == cards[i][0]:
            if PIN == cards[i][1]:
                tk.messagebox.showinfo("Success", "Successful login") #Replace with code that prompts user to enter the amount they wish to withdraw
                CurrentAccount = cards[i]
                TopLabel.config(text="Please enter Withdraw Amount") 
                Withdraw_Amount = tk.Button(ATM_Home, text="Withdraw", command=lambda: withdraw(int(TextBox.get())))
                Withdraw_Amount.place(relx=0.75,rely=0.825)
            else:
                tk.messagebox.showinfo("Error!", "Incorrect PIN entered. Please try again.")

        #Else statement shouldn't be needed since the card number would have already been checked prior to this function being called

        i+=1
    TextBox.delete(0, END)



#Display Text Box for user to enter card number in
TextBox = tk.Entry(ATM_Home,width=30)
TextBox.place(relx=0.3225,rely=0.25)


PinBox = tk.Entry()


#Create the welcome page

TopLabel = tk.Label(ATM_Home, text="Welcome, please insert card in ATM to continue") #Create a label widget
TopLabel.place(relx=0.5,rely=0.125, anchor="center")


#Create the Keypad

def insert_num(text):
    TextBox.insert(tk.INSERT, text)

def backspace():
    index = int(TextBox.index(tk.INSERT))- 1
    TextBox.delete(index)

KeypadButton1 = tk.Button(ATM_Home, text="1", command=lambda: insert_num(1)).place(relx=0.4,rely=0.4, anchor="center")
KeypadButton2 = tk.Button(ATM_Home, text="2", command=lambda: insert_num(2)).place(relx=0.5,rely=0.4, anchor="center")
KeypadButton3 = tk.Button(ATM_Home, text="3", command=lambda: insert_num(3)).place(relx=0.6,rely=0.4, anchor="center")
KeypadButton4 = tk.Button(ATM_Home, text="4", command=lambda: insert_num(4)).place(relx=0.4,rely=0.5, anchor="center")
KeypadButton5 = tk.Button(ATM_Home, text="5", command=lambda: insert_num(5)).place(relx=0.5,rely=0.5, anchor="center")
KeypadButton6 = tk.Button(ATM_Home, text="6", command=lambda: insert_num(6)).place(relx=0.6,rely=0.5, anchor="center")
KeypadButton7 = tk.Button(ATM_Home, text="7", command=lambda: insert_num(7)).place(relx=0.4,rely=0.6, anchor="center")
KeypadButton8 = tk.Button(ATM_Home, text="8", command=lambda: insert_num(8)).place(relx=0.5,rely=0.6, anchor="center")
KeypadButton9 = tk.Button(ATM_Home, text="9", command=lambda: insert_num(9)).place(relx=0.6,rely=0.6, anchor="center")
KeypadButton0 = tk.Button(ATM_Home, text="0", command=lambda: insert_num(0)).place(relx=0.5,rely=0.7, anchor="center")
Decimal = tk.Button(ATM_Home, text=".", command=lambda: insert_num(".")).place(relx=0.4,rely=0.7, anchor="center")
Backspace = tk.Button(ATM_Home, text="<----", command=backspace).place(relx=0.6,rely=0.7, anchor="center")



def insert_pin(text):
    PinBox.insert(tk.INSERT, text)

def backspace2():
    index = int(TextBox.index(tk.INSERT))- 1
    PinBox.delete(index)

def withdraw(amount):

    if(amount > 1000):
        tk.messagebox.showinfo("Error", "Amount exceeds maximum single withdrawal amount, please enter an amount less than $1000")
        TextBox.delete(0, END)

    elif(amount % 5 != 0):
        tk.messagebox.showinfo("Error", "ATM can only dispend $100, $50, $20, $10 and $5 bills, please insert a valid amount")
        TextBox.delete(0, END)

    if(amount > CurrentAccount[3]):
        # If amount exceeds the total amount of cash in the ATM
        if(amount > Total):
            tk.messagebox.showinfo("Error", "Sorry, amount exceeds current cash available within ATM")    
        else:
            total = amount
            Total - total

            # Get number of $100 bills
            num_of_100 = int(total/100)
            if(hundred_dollar_bills - num_of_100 < 0):
                num_of_100 = hundred_dollar_bills
            else:
                hundred_dollar_bills - num_of_100
                total = total - 100*num_of_100

            # Get number of $50 bills
            num_of_50 = int(total/50)
            if(fifty_dollar_bills - num_of_50 < 0):
                num_of_50 = fifty_dollar_bills
            else:
                fifty_dollar_bills - num_of_50
                total = total - 50*num_of_50

            # Get number of $20 bills
            num_of_20 = int(total/20)
            if(twenty_dollar_bills - num_of_20 < 0):
                num_of_20 = twenty_dollar_bills
            else:
                twenty_dollar_bills - num_of_20
                total = total - 20*num_of_20

            # Get number of $10 bills
            num_of_10 = int(total/10)
            if(ten_dollar_bills - num_of_10 < 0):
                num_of_10 = ten_dollar_bills
            else:
                ten_dollar_bills - num_of_10
                total = total - 10*num_of_10

            # Get number of $5 bills
            num_of_5 = int(total/5)
            if(five_dollar_bills - num_of_5 < 0):
                num_of_5 = five_dollar_bills
            else:
                five_dollar_bills - num_of_5
                total = total - 5*num_of_5
            
            # If the ATM lacks enough of certain bills
            if(total != 0):
                notEnough = "ATM is missing certain bills, could only dispense %d" % (amount - total)
                tk.messagebox.showinfo("Warning", notEnough)

            dispensedAmount = "ATM dispensed: %d $100 bills, %d $50 bills, %d $20 blills, %d $10 bills and %d $5 bils" % (num_of_100, num_of_50, num_of_20, num_of_10, num_of_5)
            tk.messagebox.showinfo("Dispensed", dispensedAmount)
            
    else: 
        tk.messagebox.showinfo("Error", "Amount exceeds your balance")
        TextBox.delete(0, END)
    

def insert_card(): 
    #Check if card is in database
    
    cardNum = TextBox.get()
    InsertedCard = cardNum
    TextBox.delete(0, END)
    
    if (cardNum in card_nums) and (check_status(cardNum)):
        
        Insert_Card.destroy()

        CurrentUser = tk.Label(ATM_Home, text="Current User:"+InsertedCard) #Create a label widget
        CurrentUser.place(relx=0.75,rely=0.075, anchor="center")
        
        TopLabel.config(text="Please enter PIN") #Create a label widget

        Enter_Pin = tk.Button(ATM_Home, text="Enter", command=lambda: check_pin(InsertedCard, TextBox.get()))
        Enter_Pin.place(relx=0.75,rely=0.825)

    else:
        tk.messagebox.showinfo("Error", "The card number entered is either invalid or not active. Please enter another card number")


Insert_Card = tk.Button(ATM_Home, text="Insert Card", command=lambda: insert_card())
Insert_Card.place(relx=0.75,rely=0.825)


ATM_Home.mainloop()

