from tkinter import*
from PIL import Image,ImageTk
from random import randint

# main window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="teal")

#picture
rock_img = ImageTk.PhotoImage(Image.open("rock3.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper3.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor3.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock3.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper3.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor3.png"))

#insert picture
user_label = Label(root,image=rock_img, bg="teal") 
comp_label = Label(root,image=paper_img_comp, bg="teal")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)


#scores
playerScore = Label(root,text=0,font=('Goudy Stout', 25, 'bold'),bg="teal",fg="black")
computerScore = Label(root,text=0,font=('Goudy Stout', 25, 'bold'),bg="teal",fg="black")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicators
user_indicator = Label(root,font=('ravie', 13, 'bold', 'underline', 'italic'),text="USER",bg="teal",fg="black")
comp_indicator = Label(root,font=('ravie', 13, 'bold', 'underline', 'italic'),text="COMPUTER",bg="teal",fg="black")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg = Label(root, font=('Arial', 20, 'bold', 'italic'),bg="teal", fg="black")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg['text'] = x

#update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

#update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)
#check winner
def checkWin(player,computer):
    if player == computer:
        updateMessage("Its a Tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("Alas! You Loose")
            updateCompScore()
        else:
            updateMessage("Hurrah!! You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("Alas! You Loose")
            updateCompScore()
        else:
            updateMessage("Hurrah!! You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("Alas! You Loose")
            updateCompScore()
        else:
            updateMessage("Hurrah!! You Win")
            updateUserScore()
    else:
        pass



#update choices

choices = ["rock","paper","scissor"]


def updateChoice(x):

#for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)



#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkWin(x,compChoice)


    
#bttons
rock = Button(root,width=20,height=2,text="ROCK",bg="lavender",fg="black", command = lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="light yellow",fg="black", command = lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="light green",fg="black", command = lambda:updateChoice("scissor")).grid(row=2,column=3)




root.mainloop()