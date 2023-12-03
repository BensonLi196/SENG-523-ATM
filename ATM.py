import tkinter as tk

ATM_Home = tk.Tk() # Main window
ATM_Home.geometry("500x500")

CardInserted = False

#Pre-loaded accounts. Format: [Card Number, Pin, Status, Balance]
card1 = ["123456", "Card1", True, "5000.00"]
card2 = ["789101112", "Card2", True, "1000.00"]
card3 = ["1314151617", "Card3", False, "850.99"]

max_allowable_withdraw = 1000

#Display Text Box for user to enter card number in
TextBox = tk.Entry(ATM_Home,width=30)
TextBox.place(relx=0.3225,rely=0.25)

index = 0; #For the keypad when typing

#Create the welcome page

Welcome_Page = tk.Label(ATM_Home, text="Welcome, please insert card in ATM to continue") #Create a label widget
Welcome_Page.place(relx=0.5,rely=0.125, anchor="center")


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
Backspace = tk.Button(ATM_Home, text="<----", command=backspace).place(relx=0.6,rely=0.7, anchor="center")


    


Insert_Card = tk.Button(ATM_Home, text="Insert Card")
Insert_Card.place(relx=0.75,rely=0.825)



ATM_Home.mainloop()
