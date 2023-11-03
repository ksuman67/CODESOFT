from tkinter import *
import string 
import random
import sys
import pyperclip

def generator(): 
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_charecters = string.punctuation
    all = small_alphabets+capital_alphabets+special_charecters
    password_length = int(length_box.get())
    
    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))
        
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
        
    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))
            
   
 
def copy():
   random_password = passwordField.get()
   pyperclip.copy(random_password)
   
def accept():
    random_password = passwordField.get()
    pyperclip.accept(random_password)   
    
def reset():
    random_password = passwordField.get()
    pyperclip.reset(random_password)

       
   
   
root = Tk()
root.config(bg = 'gray')
choice = IntVar()
Font = ('arial',13,'bold')

passworLabel = Label(root , text =' Generated Password ', font =('times new roman',20,'bold'),bg = 'gray', fg ='white')
passworLabel.grid(pady=10)

lowradioButton = Radiobutton(root,text='LOW',value=1,variable=choice,font = Font)
lowradioButton.grid(pady=5)

mediumradioButton = Radiobutton(root,text='MEDIUM',value=2,variable=choice,font = Font)
mediumradioButton.grid(pady=5)

highradioButton = Radiobutton(root,text='HIGH',value=3,variable=choice,font = Font)
highradioButton.grid(pady=5)

lengthLabel = Label(root , text ='Password Length', font = Font , bg = 'gray', fg ='white')
lengthLabel.grid(pady=5)

length_box = Spinbox(root,from_= 8, to_=20,width=5,font=Font)
length_box.grid(pady=5)

generateButton = Button(root,text=' Generate Password',font = Font, command = generator)
generateButton.grid(pady=5)

passwordField = Entry(root,width=25,bd=2,font = Font)
passwordField.grid()

acceptButton = Button(root,text='ACCEPT',font = Font,command = accept)
acceptButton.grid(pady=5)

resetButton = Button(root,text=' RESET ',font = Font)
resetButton.grid(pady=5)


copyButton = Button(root,text='COPY',font = Font)
copyButton.grid(pady=5)

root.mainloop()
