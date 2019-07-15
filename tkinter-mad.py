#import tkinter for graphics
from tkinter import *

#list for questions and answers
questions = ['Enter an adjective related to weather....', 'Enter a number between 100 and 300...', 'Enter a number between 10 and 20...', 'Enter the name of a song...','Enter an adjective...', 'Enter an adjective relating to evil...', 'Enter the name of the person closest to you...', 'Enter a number between 1000 and 4000...', 'Enter an adjective related to prison...']
answers = []

#function for when submit button is clicked
def click(self):
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


#create tkinter window, set title, background color, and size
window = Tk()
window.title('Mad-Libs')
window.configure(background='black')
window.geometry('1000x600')


window.bind('<Return>', click)

#initialize question numbers and initial question
q_act = StringVar()
q_act.set(questions[0])

q_num_str = StringVar()
q_num_str.set("Question 1 of "+str(len(questions)))
q_num = 1

#enter will cause the click function to run
# NEED TO FIX !!!!!!!!!!!!!
#window.bind('<Return>',click)

#title
Label(window,text='Mad-Libs',bg='black',fg='#1eeeff',font='Roboto 50 bold').pack(pady='10')

#question text
Label(window,textvariable=q_act,bg='black',fg='#1eeeff',font='Courier 20').pack(pady='10')

#entry box for text
textentry = Entry(window,width=20,bg='white',font='Courier 16')
textentry.pack(pady='20')

Label(window,textvariable=q_num_str,bg='black',fg='blue',font='Roboto 20').pack(pady='10')
#submit button

Button(window,text='SUBMIT',width=10,command=click).pack()


#question number and instructions on the bottom
Label(window, bg='black',fg='#f542ad',text='Created by: BL4Z3, h4ckerm4n_z4ch, b1g n@te, and PW3Z',font='Courier 18').pack(side='bottom',pady='10')

Label(window,bg='black',fg='white',text='Answer the question in the text box and press enter',font='Courier 15').pack(side="bottom")



#begin main GUI loop
window.mainloop()
