from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='sandip' and passwordEntry.get()=='1234':
        messagebox.showinfo(('Success','welcome'))
        window.destroy()
        import sms

    else:
        messagebox.showinfo('Error','please enter correct data')

window = Tk()

window.geometry('1280x700+0+0')
window.title('login System of School management System')

window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bglabel = Label(window, image=backgroundImage)
bglabel.place(x=0, y=0)

loginFrame = Frame(window,bg='white')
loginFrame.place(x=400, y=150)

logoImage = PhotoImage(file='logo.png')

logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file='username.png')
usernameLabel = Label(loginFrame,image=usernameImage,text='Username',compound=LEFT
                      ,font=('time new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,padx=20)

usernameEntry=Entry(loginFrame,font=('time new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage=PhotoImage(file='password.png')
passwordLabel = Label(loginFrame,image=passwordImage,text='password',compound=LEFT
                      ,font=('time new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,padx=20)

passwordEntry=Entry(loginFrame,font=('time new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='login',font=('times new roman',14,'bold'),width=15
                   ,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',
                   activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)


window.mainloop()


