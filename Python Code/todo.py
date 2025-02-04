from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')
        self.root.configure(bg='ivory')

        self.label = Label(self.root, text='To-Do-List-Manager', font=('Arial', 25, 'bold', 'underline', 'italic'), bg='pink', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add task', font=('Arial', 18, 'bold'), bg='pink', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks', font=('Arial', 18, 'bold'), bg='pink', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=8, bd=5, width=23, font=('Arial', 20, 'italic', 'bold'))
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font=('Arial', 10, 'bold'))
        self.text.place(x=20, y=120)

        def add():
            content = self.text.get(1.0, END).strip()
            if content:
                content = content + " [not done]"
                self.main_text.insert(END, content)
                with open("data.txt", "a") as file:
                    file.write(content + '\n')
                self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            if delete_:
                look = self.main_text.get(delete_)
                self.main_text.delete(delete_)
                with open("data.txt", "r") as f:
                    lines = f.readlines()
                with open("data.txt", "w") as f:
                    for line in lines:
                        if line.strip() != look:
                            f.write(line)
        def update():
            selected_index = self.main_text.curselection()
            if selected_index:
                content = self.main_text.get(selected_index)
                if "[not done]" in content:
                    new_content = content.replace("[not done]", "[done]")
                elif "[done]" in content:
                    new_content = content.replace("[done]", "[not done]")
                else:
                    new_content = content + " [done]"

                self.main_text.delete(selected_index)
                self.main_text.insert(selected_index, new_content)

                with open("data.txt", "r") as f:
                    lines = f.readlines()
                with open("data.txt", "w") as f:
                    for line in lines:
                        if line.strip() != content:
                            f.write(line)
                    f.write(new_content + '\n')



        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    self.main_text.insert(END, line.strip())
        except FileNotFoundError:
            open('data.txt', 'w').close()

        self.add_button = Button(self.root, text="Add", font=('Arial', 20, 'bold', 'italic'), width=10, bd=5, bg='pink', fg='black', command=add)
        self.add_button.place(x=30, y=180)

        self.delete_button = Button(self.root, text="Delete", font=('Arial', 20, 'bold', 'italic'), width=10, bd=5, bg='pink', fg='black', command=delete)
        self.delete_button.place(x=30, y=250)

        self.button3 = Button(self.root, text="Update", font=('Arial', 20, 'bold', 'italic'),width=10, bd=5, bg="pink", fg="black", command=update)
        self.button3.place(x=30, y=320)

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
