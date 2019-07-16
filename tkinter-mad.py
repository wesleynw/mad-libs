#import tkinter for graphics
from tkinter import *

#list for questions and answers
q_area51 = ['Enter an adjective related to weather...', 'Enter a number between 100 and 300...', 'Enter a number between 10 and 20...', 'Enter the name of a song...', 'Enter an adjective relating to birthday parties...', 'Enter an adjective relating to evil...', 'Enter the name of the person physically closest to you...', 'Enter a number between 1000 and 4000...', 'Enter an adjective that reminds you of prison...', 'Fortnite kids or anti-vax kids...', 'Enter an adjective related to anger...']
questions = q_area51
answers = []

#function for when submit button is clicked
def click(self):
    if(lbl1.winfo_ismapped()):
            begin(self)
            return 0

    #append answer from textbox to answers list
    answers.append(textentry.get())

    #empty text box
    textentry.delete(0, END)

    #add one to the question number
    global q_num
    q_num+=1

    #return string for question number and move to next question text
    q_num_str.set('Question '+str(q_num)+' of '+str(len(questions)))
    q_act.set(questions[q_num-1])

    if q_num == len(questions):
        #run clear screen and show story
        #window.withdraw()
        #input.destroy()
        var1 = 0

#move to normal game, delete beginning and play button
def begin(self):
    lbl1.pack_forget()
    lbl2.pack_forget()

#create tkinter window, set title, background color, and size
window = Tk()
window.title('Mad-Libs')
window.configure(background='black')
window.geometry('1000x600')

#start screen with images
img = PhotoImage(file='bg_1000x600.png')
img2 = PhotoImage(file='begin_1000x.png')
lbl1 = Label(window,image=img2,bg='black')
lbl1.pack(side='bottom')
lbl2 = Label(window,image=img,bg='black')
lbl2.pack()

#enter button does the same thing as the submit button
window.bind('<Return>', click)
window.bind('<Button-1>',begin)

#title
Label(window,text='Mad-Libs',bg='black',fg='red',font='Courier 50 bold').pack(pady='10')

#initialize question numbers and initial question
q_act = StringVar()
q_act.set(questions[0])

q_num_str = StringVar()
q_num_str.set("Question 1 of "+str(len(questions)))
q_num = 1

#question text
Label(window,textvariable=q_act,bg='black',fg='red',font='Courier 20').pack(pady='10')

#entry box for text
input = textentry = Entry(window,width=20,bg='white',font='Courier 16')
input.pack(pady='20')

#question number string
Label(window,textvariable=q_num_str,bg='black',fg='red',font='Roboto 20').pack(pady='10')

#submit button
Button(window,text='SUBMIT',width=10,command=click).pack()

#question number and instructions on the bottom
Label(window, bg='black',fg='red',text='Created by: BL4Z3, h4ckerm4n_z4ch, b1g n@te, and PW3Z',font='Courier 18').pack(side='bottom',pady='10')

Label(window,bg='black',fg='white',text='Answer the question in the text box and press enter',font='Courier 15').pack(side="bottom")

#begin main GUI loop
window.mainloop()
