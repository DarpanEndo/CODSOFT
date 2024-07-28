import string 
import random
import tkinter as tk

class MainWindow:
    def __init__(self):
        self.main = tk.Tk()
        self.main.geometry("300x350")
        self.main.resizable(width=False, height=False)
        self.main.title("Password Generator")
        self.widgets()
        self.main.mainloop()

    def widgets(self):
        self.frame = tk.Frame(self.main)

        self.val, self.special, self.num = tk.IntVar(), tk.IntVar(), tk.IntVar()
        self.optionsFrame = tk.LabelFrame(self.frame, text="Options")
        self.uppercase = tk.Checkbutton(self.optionsFrame, text="Uppercase Letters", onvalue=1, offvalue=0, variable=self.val)
        self.specialChar = tk.Checkbutton(self.optionsFrame,text="Special Characters", onvalue=1, offvalue=0, variable=self.special)
        self.number = tk.Checkbutton(self.optionsFrame, text="Number", onvalue=1, offvalue=0, variable=self.num)

        self.length = tk.IntVar()
        self.lengthFrame = tk.LabelFrame(self.frame, text="Pwd Length")
        self.radioButton1 = tk.Radiobutton(self.lengthFrame, text="10",value=10, variable=self.length)
        self.radioButton2 = tk.Radiobutton(self.lengthFrame, text="12",value=12, variable=self.length)
        self.radioButton3 = tk.Radiobutton(self.lengthFrame, text="16",value=16, variable=self.length)
        self.length.set("10")
        
        self.genPwd = tk.Button(self.main, text="Generate Password", width=25, command=self.generatePassword)
        self.viewHistory = tk.Button(self.main, text="View History", width=25, command=self.getHistory)
        self.textBox = tk.Text(self.main, width=25, height=8, relief="solid") 

        self.widgetsInFrame = [ self.uppercase, self.specialChar, self.number ]
        for item in self.widgetsInFrame: item.pack(pady=5, anchor="w")

        self.radioButtons = [ self.radioButton1, self.radioButton2, self.radioButton3 ]
        for radioButton in self.radioButtons: radioButton.pack(pady=5, anchor="w")

        self.optionsFrame.grid(row=0, column=0)
        self.lengthFrame.grid(row=0, column=1)

        self.mainWidgets = [ self.frame, self.genPwd, self.viewHistory, self.textBox ]
        for widget in self.mainWidgets: widget.pack(pady=5)

    def generatePassword(self):
        if self.val.get() ==1:
            randomUpper = random.choices(string.ascii_uppercase, k=5)
        else: randomUpper = []
        if self.special.get() == 1:
            randomSpecial = random.choices("-@!?.", k=2)
        else: randomSpecial = []
        if self.num.get() == 1:
            randomNum = random.choices(string.digits, k=5)
        else: randomNum = []

        randomGen = random.sample(randomUpper+randomSpecial+randomNum+random.choices(string.ascii_lowercase, k=16), k=int(self.length.get()))
        self.textBox.config(state="normal")
        self.textBox.insert(1.0,f"{ ''.join(randomGen)}\n")
        self.textBox.config(state="disabled")
        with open("password.txt", "a") as file: file.write(f"{"".join(randomGen)}\n")

    def getHistory(self):
        self.textBox.config(state="normal")
        self.textBox.delete(1.0,"end")
        self.textBox.insert(1.0, open ("password.txt", "r").read())
        self.textBox.config(state="disabled")



        
        









if __name__ == '__main__':
    MainWindow()

