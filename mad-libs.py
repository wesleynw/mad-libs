#import tkinter for graphics
from tkinter import *

#list for questions and answers
answers = []
q_area51 = ['Enter an adjective related to weather...', 'Enter a number between 100 and 300...', 'Enter a number between 10 and 20...', 'Enter the name of a song...', 'Enter an adjective relating to birthday parties...', 'Enter an adjective relating to evil...', 'Enter the name of the person physically closest to you...', 'Enter a number between 1000 and 4000...', 'Enter an adjective that reminds you of prison...', 'Fortnite kids or anti-vax kids...', 'Enter an adjective related to anger...']
s_area51 = """It was the morning of September 20th, 2019. Yet the sun didn't rise. The """+answers[0]

#the question list should be set equal to the set which is being used
questions = q_area51

def write_story():
        q_num_label.pack_forget()
        #question text
        q_text.pack_forget()
        #delete text field
        q_input.pack_forget()
        #delete submit button
        submit_button.pack_forget()
        #delete bottom label
        bottom_label.pack_forget()




#function for when submit button is clicked
def click(self):
    #append answer from textbox to answers list
    answers.append(q_input.get())

    #empty text box
    q_input.delete(0, END)

    #specify q_num as a global variable so it can be edited
    global q_num
    #add one to the question number
    q_num+=1

    #once questions are all answered, delete question number field
    if q_num > len(questions):
        write_story()
        
    #return string for question number and move to next question text
    q_num_str.set('Question '+str(q_num)+' of '+str(len(questions)))
    q_act.set(questions[q_num-1])

#create tkinter window, set title, background color, and size
window = Tk()
window.title('Mad-Libs')
window.configure(background='black')
window.geometry('1000x600')

#enter button does the same thing as the submit button
window.bind('<Return>', click)

#title
Label(window,text='Mad-Libs',bg='black',fg='red',font='Courier 50 bold').pack(pady='10')

#initialize question numbers and initial question
q_act = StringVar()
q_act.set(questions[0])

q_num_str = StringVar()
q_num_str.set("Question 1 of "+str(len(questions)))
q_num = 1

#question text
q_text = Label(window,textvariable=q_act,bg='black',fg='red',font='Courier 20')
q_text.pack(pady='10')

#entry box for text
q_input = Entry(window,width=20,bg='white',font='Courier 16')
q_input.pack(pady='20')

#question number string
q_num_label = Label(window,textvariable=q_num_str,bg='black',fg='red',font='Roboto 20')
q_num_label.pack(pady='10')

#submit button
submit_button = Button(window,text='SUBMIT',width=10,command=click)
submit_button.pack()

#question number and instructions on the bottom
Label(window, bg='black',fg='red',text='Created by: BL4Z3, h4ckerm4n_z4ch, b1g n@te, and PW3Z',font='Courier 18').pack(side='bottom',pady='10')

bottom_label = Label(window,bg='black',fg='white',text='Answer the question in the text box and press enter',font='Courier 15')
bottom_label.pack(side='bottom')

#begin main GUI loop
window.mainloop()
